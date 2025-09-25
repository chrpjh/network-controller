#!/usr/bin/env bash
set -euo pipefail


# Defaults
NS="nvidia-network-operator" # Operator namespace
VENDOR="15b3" # NVIDIA/Mellanox
VFS_PER_PF=1 # PF당 VF 개수 (DL 학습이면 1 권장)
RESOURCE_PREFIX="ten1010.io" # node.status.capacity에 노출될 prefix


# Arrays of mappings: "<PF_NAME>:<RESOURCE_NAME>"
ETH_PFS=()
IB_PFS=()


usage(){ cat <<USAGE
Usage: $0 [options]
--namespace <ns> Operator namespace (default: ${NS})
--vendor <hex> PCI vendor (default: ${VENDOR})
--vfs-per-pf <N> Number of VFs per PF (default: ${VFS_PER_PF})
--resource-prefix <domain> Resource prefix (default: ${RESOURCE_PREFIX})
--eth-pf <pf:res> Ethernet PF→resource (repeatable). ex: --eth-pf ens2f0np0:netif-eth100g
--ib-pf <pf:res> InfiniBand PF→resource (repeatable). ex: --ib-pf ibs1f0:netif-ib200g
-h|--help
USAGE
}


parse_pf_arg(){
local arg="$1"; local arrname="$2"
[[ "$arg" == *:* ]] || { echo "ERROR: must be PF:RESOURCE" >&2; exit 1; }
local pf="${arg%%:*}"; local res="${arg##*:}"
[[ -n "$pf" && -n "$res" ]] || { echo "ERROR: invalid PF mapping '$arg'" >&2; exit 1; }
if [[ "$arrname" == "ETH_PFS" ]]; then ETH_PFS+=("$pf:$res"); else IB_PFS+=("$pf:$res"); fi
}


while [[ $# -gt 0 ]]; do
case "$1" in
--namespace) NS="$2"; shift 2;;
--vendor) VENDOR="$2"; shift 2;;
--vfs-per-pf) VFS_PER_PF="$2"; shift 2;;
--resource-prefix) RESOURCE_PREFIX="$2"; shift 2;;
--eth-pf) parse_pf_arg "$2" ETH_PFS; shift 2;;
--ib-pf) parse_pf_arg "$2" IB_PFS; shift 2;;
-h|--help) usage; exit 0;;
*) echo "Unknown arg: $1"; usage; exit 1;;
esac
done


command -v kubectl >/dev/null || { echo "kubectl not found"; exit 1; }


# --- Build sriovDevicePlugin.config JSON (group by resource name) ---
build_resource_json(){
local linktype="$1" # ETH or IB
shift
local -a items=("$@")
declare -A res_to_pfs
for m in "${items[@]}"; do
local pf="${m%%:*}"; local res="${m##*:}"
res_to_pfs["$res"]+="$pf,"
done
local first=1
for res in "${!res_to_pfs[@]}"; do
local pfs_csv="${res_to_pfs[$res]}"; pfs_csv="${pfs_csv%,}"
[[ $first -eq 1 ]] || echo ","
first=0
cat <<J
{
"resourcePrefix": "${RESOURCE_PREFIX}",
"resourceName": "${res}",
"selectors": {
"vendors": ["${VENDOR}"],
"linkTypes": ["${linktype}"],
"pfNames": [${pfs_csv//,/","}]
}
}
J
done
}


ETH_JSON=$(build_resource_json "ETH" "${ETH_PFS[@]}" || true)
IB_JSON=$(build_resource_json "IB" "${IB_PFS[@]}" || true)
echo "\n[NOTE] Device Plugin은 capacity만 올립니다. 실제 NIC 부착(NAD)은 Multus 혹은 웹훅에서 처리하세요."