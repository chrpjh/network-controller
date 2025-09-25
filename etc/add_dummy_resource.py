from kubernetes.config import load_kube_config
from kubernetes.client import CoreV1Api

node_list = [
    "vnode2.pnode2.idc1.ten1010.io",
    "vnode2.pnode7.idc1.ten1010.io",
    "vnode1.pnode7.idc1.ten1010.io",
    "vnode2.pnode6.idc1.ten1010.io"
]

load_kube_config()

api = CoreV1Api()

body = {
    "status": {
        "capacity": {
            "ten1010.io/netif-ib-400g-sid1": 4,
            "ten1010.io/netif-ib-400g-sid2": 4,
            "ten1010.io/netif-eth-100g-sid3": 4,
            "ten1010.io/netif-eth-400g-sid4": 4,
            "ten1010.io/netif-ib-400g-sid1": 4,
            "ten1010.io/netif-ib-400g-sid1": 4,
            "ten1010.io/netif-ib-400g-sid1": 4
        }
    }
}
api.patch_node_status(name="")
