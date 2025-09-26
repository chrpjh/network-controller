from controller import Controller

from pks.common.utils import set_no_buffer_stream
from pks.k8s.client.configuration import load_config_from_secret
from pks.k8s.client.configuration import load_models


if __name__ == "__main__":
    set_no_buffer_stream()
    load_config_from_secret()
    load_models()
    controller = Controller()
    controller.run()






"""

Pkey는 네트워크 오퍼레이터랑 별개로 동작해야될 듯




1. Nvidia 네트워크 오퍼레이터 설치
2. NIC 서치해서 리스트 뽑음
3. 위의 리스트에서 리소스로 쓸 것만 뽑아서 config로 만듦
4. config를 기반으로 


"""