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
