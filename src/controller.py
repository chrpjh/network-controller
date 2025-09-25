import time
import threading

from kubernetes.client import CoreV1Api
from kubernetes.client import RbacAuthorizationV1Api
from pks.k8s.client.custom_object_api import CustomObjectApi
from pks.k8s.controller.informer import Informer
from pks.k8s.webhook.webhook import Webhook
from pks.common.logger import Logger

import config
from models.aipub_user import AIPubUser
from models.aipub_user import AIPubUserList
from models.project import Project
from models.project import ProjectList
from mutate.user_label import UserLabelMutateService
from mutate.user_owner import UserOwnerReferenceMutateService
from mutate.user_transfer import UserTransferMutateService
from mutate.user_authority_review import UserAuthorityReviewMutateService
from mutate.workload_label import WorkloadLabelMutateService
from validate.user_label import UserLabelValidateService
from validate.user_authority_review import UserAuthorityReviewValidateService
from aipub_user_service import AIPubUserService
from owner_service import OwnerService
from api_resource_manager import APIResourceManager


class Controller(object):

    def __init__(self):
        self._load_waiting_second = config.INFORMER_LOAD_WAITING_SECOND
        core_api = CoreV1Api()
        custom_api = CustomObjectApi()
        rbac_api = RbacAuthorizationV1Api()
        aipub_user_service = AIPubUserService()
        api_resource_manager = APIResourceManager()
        owner_service = OwnerService(api_resource_manager=api_resource_manager)
        namespace_informer = Informer(
            object_kind="Namespace",
            func=core_api.list_namespace
        )
        clusterrolebinding_informer = Informer(
            object_kind="ClusterRoleBinding",
            func=rbac_api.list_cluster_role_binding
        )
        clusterrole_informer = Informer(
            object_kind="ClusterRole",
            func=rbac_api.list_cluster_role
        )
        rolebinding_informer = Informer(
            object_kind="RoleBinding",
            func=rbac_api.list_role_binding_for_all_namespaces
        )
        role_informer = Informer(
            object_kind="Role",
            func=rbac_api.list_role_for_all_namespaces
        )
        user_informer = Informer(
            object_kind="AipubUser",
            func=custom_api.list_cluster_custom_object,
            model_class=AIPubUser,
            model_list_class=AIPubUserList,
            group=config.AIPUB_USER_API_GROUP,
            version=config.AIPUB_USER_API_VERSION,
            plural=config.AIPUB_USER_API_PLURAL
        )
        project_informer = Informer(
            object_kind="Project",
            func=custom_api.list_cluster_custom_object,
            model_class=Project,
            model_list_class=ProjectList,
            group=config.PROJECT_API_GROUP,
            version=config.PROJECT_API_VERSION,
            plural=config.PROJECT_API_PLURAL
        )
        self._informers = [
            namespace_informer,
            clusterrolebinding_informer,
            clusterrole_informer,
            rolebinding_informer,
            role_informer,
            user_informer,
            project_informer
        ]
        user_label_mutate_service = UserLabelMutateService(
            aipub_user_service=aipub_user_service,
            owner_service=owner_service
        )
        user_owner_mutate_service = UserOwnerReferenceMutateService(
            aipub_user_service=aipub_user_service
        )
        user_transfer_mutate_service = UserTransferMutateService(
            aipub_user_service=aipub_user_service
        )
        user_authority_review_mutate = UserAuthorityReviewMutateService(
            user_informer=user_informer,
            project_informer=project_informer,
            namespace_informer=namespace_informer,
            clusterrolebinding_informer=clusterrolebinding_informer,
            clusterrole_informer=clusterrole_informer,
            rolebinding_informer=rolebinding_informer,
            role_informer=role_informer,
            api_resource_manager=api_resource_manager
        )
        workload_label_mutate_service = WorkloadLabelMutateService(
            owner_service=owner_service
        )

        user_label_validate_service = UserLabelValidateService()
        user_authority_review_validate = UserAuthorityReviewValidateService()

        self._webhook = Webhook()
        self._webhook.add_mutate_service(
            mutate_service=user_label_mutate_service
        )
        self._webhook.add_mutate_service(
            mutate_service=user_owner_mutate_service
        )
        self._webhook.add_mutate_service(
            mutate_service=user_transfer_mutate_service
        )
        self._webhook.add_mutate_service(
            mutate_service=user_authority_review_mutate
        )
        self._webhook.add_mutate_service(
            mutate_service=workload_label_mutate_service
        )
        self._webhook.add_validate_service(
            validate_service=user_label_validate_service
        )
        self._webhook.add_validate_service(
            validate_service=user_authority_review_validate
        )
        self._logger = Logger(name="AdmissionController")

    def run(self):
        for informer in self._informers:
            informer.run()

        is_all_loaded = False
        for _ in range(self._load_waiting_second):
            all_loaded = True
            for informer in self._informers:
                if not informer.is_loaded:
                    all_loaded = False
                    break
            if all_loaded:
                is_all_loaded = True
                break
            time.sleep(1)
        if not is_all_loaded:
            raise Exception("Informer load failed")

        webhook = threading.Thread(
            target=self._webhook.run, daemon=True
        )
        webhook.start()

        self._logger.info("Controller Started")
        is_stopped = False
        while not is_stopped:
            if not webhook.is_alive():
                is_stopped = True
            for informer in self._informers:
                if informer.is_stopped():
                    is_stopped = True
                    break
            if not is_stopped:
                time.sleep(2)
        self._logger.info("Controller Stopped")
