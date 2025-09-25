from kubernetes.client import ApiClient
from pks.k8s.webhook.mutate_service import MutateService
from pks.k8s.webhook.mutate_service import MutateServiceOutput
from pks.common.logger import Logger

import config
from owner_service import OwnerService


class WorkloadLabelMutateService(MutateService):

    def __init__(self, owner_service):
        if not isinstance(owner_service, OwnerService):
            raise TypeError()
        self._api_client = ApiClient()
        self._workload_name_label_key = config.AIPUB_WORKLOAD_NAME_LABEL_KEY
        self._workload_kind_label_key = config.AIPUB_WORKLOAD_KIND_LABEL_KEY
        self._owner_service = owner_service
        self._logger = Logger(name="WorkloadLabelMutateService")

    def _get_workload_labels_from_owner(self, owner_object):
        labels = owner_object["metadata"].get("labels")
        if labels is None:
            return
        workload_name = labels.get(self._workload_name_label_key)
        if workload_name is None:
            return
        workload_kind = labels.get(self._workload_kind_label_key)
        if workload_kind is None:
            return
        workload_labels = {
            self._workload_name_label_key: workload_name,
            self._workload_kind_label_key: workload_kind
        }
        return workload_labels

    def mutate(self, request):
        output = MutateServiceOutput(allowed=True)
        if request.operation != "CREATE":
            return output

        if not request.namespace:
            return output

        mutated_obj = request.obj

        owner_object = self._owner_service.get_owner_object(
            obj=mutated_obj, namespace=request.namespace, output=output
        )
        if not output.allowed or owner_object is None:
            return output

        workload_labels = self._get_workload_labels_from_owner(
            owner_object=owner_object
        )
        if workload_labels is None:
            workload_name = owner_object["metadata"]["name"]
            workload_kind = owner_object["kind"]
            workload_labels = {
                self._workload_name_label_key: workload_name,
                self._workload_kind_label_key: workload_kind
            }

        labels = mutated_obj["metadata"].get("labels")
        if labels is None:
            labels = {}
            mutated_obj["metadata"]["labels"] = labels
        labels.update(workload_labels)
        output.to_allowed(mutated_obj=mutated_obj)
        return output
