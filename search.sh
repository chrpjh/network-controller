#!/bin/bash
# SR-IOV 지원 NIC 탐색 스크립트
# PF + SR-IOV + 속도 확인 + Ethernet/Infiniband 타입 구분

echo "=== SR-IOV 지원 NIC 스펙 탐색 시작 ==="

for iface in $(ls /sys/class/net/ | grep -v '^lo$'); do
  dev_path="/sys/class/net/$iface/device"

  # VF (가상 인터페이스)는 제외
  if [[ -e "$dev_path/physfn" ]]; then
    continue
  fi

  # SR-IOV 지원 여부 확인
  if [[ -f "$dev_path/sriov_totalvfs" ]]; then
    totalvfs=$(cat $dev_path/sriov_totalvfs)
  else
    continue
  fi

  # 드라이버 확인
  driver=$(ethtool -i $iface 2>/dev/null | grep "driver:" | awk '{print $2}')

  # 속도 확인
  speed=$(ethtool $iface 2>/dev/null | grep "Speed:" | awk '{print $2}')

  # 속도 정보 없는 경우는 제외
  if [[ "$speed" == "Unknown!" || -z "$speed" ]]; then
    continue
  fi

  # 타입 판별: Infiniband (ib_ipoib) vs Ethernet
  if ethtool -i $iface 2>/dev/null | grep -q "ib_ipoib"; then
    type="Infiniband"
  else
    type="Ethernet"
  fi

  echo "--------------------------------"
  echo "Interface : $iface"
  echo "Type      : $type"
  echo "Driver    : $driver"
  echo "Speed     : $speed"
  echo "SR-IOV VF : $totalvfs"
done

echo "=== SR-IOV 지원 NIC 스펙 탐색 완료 ==="
