from kubernetes.config import load_kube_config
from kubernetes.client import CoreV1Api


load_kube_config()

api = CoreV1Api()

body = {
    "status": {
        "capacity": {
            "ten1010.io/netif-ib-400g-sid1": 4,
            "ten1010.io/netif-ib-400g-sid2": 4,
            "ten1010.io/netif-eth-100g-sid3": 1,
            "ten1010.io/netif-eth-10g-sid4": 1,
        }
    }
}
node_name = "vnode2.pnode2.idc1.ten1010.io"

api.patch_node_status(name=node_name, body=body)
