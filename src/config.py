import os


USER_AUTHORITY_REVIEW_GROUP = "aipub.ten1010.io"
USER_AUTHORITY_REVIEW_VERSION = "v1alpha1"
USER_AUTHORITY_REVIEW_KIND = "UserAuthorityReview"

USERNAME_LABEL_KEY = os.getenv(
    "USERNAME_LABEL_KEY", "aipub.ten1010.io/username"
)
USERID_LABEL_KEY = os.getenv(
    "USERID_LABEL_KEY", "aipub.ten1010.io/userid"
)
USER_API_GROUP = os.getenv(
    "USER_API_GROUP", "project.aipub.ten1010.io"
)
USER_API_VERSION = os.getenv(
    "USER_API_VERSION", "v1alpha1"
)
USER_API_PLURAL = os.getenv(
    "USER_API_PLURAL", "aipubusers"
)
PROJECT_API_GROUP = os.getenv(
    "PROJECT_API_GROUP", "project.aipub.ten1010.io"
)
PROJECT_API_VERSION = os.getenv(
    "PROJECT_API_VERSION", "v1alpha1"
)
PROJECT_API_PLURAL = os.getenv(
    "PROJECT_API_PLURAL", "projects"
)
ADMIN_USER_GROUP_NAME = os.getenv(
    "ADMIN_USER_GROUP_NAME", "oidc:aipub-admin"
)
MEMBER_USER_GROUP_NAME = os.getenv(
    "MEMBER_USER_GROUP_NAME", "oidc:aipub-member"
)
AIPUB_USER_NAME_DELIMITER = os.getenv(
    "AIPUB_USER_NAME_DELIMITER", ":"
)
INFORMER_LOAD_WAITING_SECOND = int(
    os.getenv("INFORMER_LOAD_WAITING_SECOND", "30")
)
API_RESOURCE_MANAGER_LOAD_PERIOD = int(
    os.getenv("API_RESOURCE_MANAGER_LOAD_PERIOD", 60)
)
API_RESOURCES_CONFIGMAP_NAME = os.getenv(
    "API_RESOURCES_CONFIGMAP_NAME", "api-resources"
)
API_RESOURCES_CONFIGMAP_NAMESPACE = os.getenv(
    "API_RESOURCES_CONFIGMAP_NAMESPACE", "aipub"
)


OWNER_REFERENCE_EXCEPT_OBJECTS = os.getenv(
    "OWNER_REFERENCE_EXCEPT_OBJECTS",
    "ImageNamespace,Project"
)
WORKSPACE_API_GROUP = os.getenv(
    "WORKSPACE_API_GROUP", "aipub.ten1010.io"
)
WORKSPACE_API_VERSION = os.getenv(
    "WORKSPACE_API_VERSION", "v1"
)
WORKSPACE_API_PLURAL = os.getenv(
    "WORKSPACE_API_PLURAL", "workspaces"
)
WORKSPACE_KIND = os.getenv("WORKSPACE_KIND", "Workspace")
FTPSERVER_API_GROUP = os.getenv(
    "FTPSERVER_API_GROUP", "aipub.ten1010.io"
)
FTPSERVER_API_VERSION = os.getenv(
    "FTPSERVER_API_VERSION", "v1"
)
FTPSERVER_API_PLURAL = os.getenv(
    "FTPSERVER_API_PLURAL", "ftpservers"
)
FTPSERVER_KIND = os.getenv("FTPSERVER_KIND", "FtpServer")
OPERATION_API_GROUP = os.getenv(
    "OPERATION_API_GROUP", "aipub.ten1010.io"
)
OPERATION_API_VERSION = os.getenv(
    "OPERATION_API_VERSION", "v1alpha1"
)
OPERATION_API_PLURAL = os.getenv(
    "OPERATION_API_PLURAL", "operations"
)
OPERATION_KIND = os.getenv("OPERATION_KIND", "Operation")

AIPUBJob_API_GROUP = os.getenv(
    "AIPUBJob_API_GROUP", "aipub.ten1010.io"
)
AIPUBJob_API_VERSION = os.getenv(
    "AIPUBJob_API_VERSION", "v1alpha1"
)
AIPUBJob_API_PLURAL = os.getenv(
    "AIPUBJob_API_PLURAL", "aipubjobs"
)
AIPUBJob_KIND = os.getenv("AIPUBJob_KIND", "AIPubJob")

AIPUB_WORKLOAD_LIST = os.getenv(
    "AIPUB_WORKLOAD_LIST", "Operation,Workspace,FtpServer,AIPubJob"
)

AIPUB_WORKLOAD_KIND_LABEL_KEY = os.getenv(
    "AIPUB_WORKLOAD_KIND_LABEL_KEY", "aipub.ten1010.io/workload-kind"
)
AIPUB_WORKLOAD_NAME_LABEL_KEY = os.getenv(
    "AIPUB_WORKLOAD_NAME_LABEL_KEY", "aipub.ten1010.io/workload-name"
)

###########

AIPUB_USER_MEMBER_GROUP = os.getenv(
    "AIPUB_USER_MEMBER_GROUP", "oidc:aipub-member"
)
AIPUB_USER_ADMIN_GROUP = os.getenv(
    "AIPUB_USER_ADMIN_GROUP", "oidc:aipub-admin"
)
AIPUB_USER_NAME_DELIMITER = os.getenv(
    "AIPUB_USER_NAME_DELIMITER", ":"
)
AIPUB_USER_NAME_LABEL_KEY = os.getenv(
    "AIPUB_USER_NAME_LABEL_KEY", "aipub.ten1010.io/username"
)
AIPUB_USER_ID_LABEL_KEY = os.getenv(
    "AIPUB_USER_ID_LABEL_KEY", "aipub.ten1010.io/userid"
)
AIPUB_USER_API_GROUP = os.getenv(
    "AIPUB_USER_API_GROUP", "project.aipub.ten1010.io"
)
AIPUB_USER_API_VERSION = os.getenv(
    "AIPUB_USER_API_VERSION", "v1alpha1"
)
AIPUB_USER_API_PLURAL = os.getenv(
    "AIPUB_USER_API_PLURAL", "aipubusers"
)
AIPUB_USER_API_KIND = os.getenv(
    "AIPUB_USER_API_KIND", "AipubUser"
)
USER_TRANSFER_ANNOTATION_KEY = os.getenv(
    "USER_TRANSFER_ANNOTATION_KEY", "user.aipub.ten1010.io/transfer"
)
