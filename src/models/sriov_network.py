from pks.k8s.client.model import model


@model
class SriovNetwork(object):

    openapi_types = {
        "api_version": "str",
        "kind": "str",
        "metadata": "V1ObjectMeta",
        "spec": "SriovNetworkSpec"
    }

    attribute_map = {
        "api_version": "apiVersion",
        "kind": "kind",
        "metadata": "metadata",
        "spec": "spec"
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None):
        self._api_version = api_version
        self._kind = kind
        self._metadata = metadata
        self._spec = spec

    @property
    def api_version(self):
        return self._api_version

    @property
    def kind(self):
        return self._kind

    @property
    def metadata(self):
        return self._metadata

    @property
    def spec(self):
        return self._spec


@model
class SriovNetworkList(object):

    openapi_types = {
        "api_version": "str",
        "kind": "str",
        "metadata": "V1ListMeta",
        "items": "list[SriovNetwork]"
    }

    attribute_map = {
        "api_version": "apiVersion",
        "kind": "kind",
        "metadata": "metadata",
        "items": "items"
    }

    def __init__(self, api_version=None, kind=None, metadata=None, items=None):
        self._api_version = api_version
        self._kind = kind
        self._metadata = metadata
        self._items = items

    @property
    def api_version(self):
        return self._api_version

    @property
    def kind(self):
        return self._kind

    @property
    def metadata(self):
        return self._metadata

    @property
    def items(self):
        return self._items
