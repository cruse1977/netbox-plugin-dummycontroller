from extras.plugins import PluginConfig
from .version import __version__

class NetBoxPluginDummyControllerConfig(PluginConfig):
    name = 'netbox_plugin_dummycontroller'
    verbose_name = 'NetBox Plugin DummyController'
    description = ''
    version = __version__
    base_url = 'plugin-helloworld'
    min_version = '4.2.0'
    max_version = '4.2.99'

    def ready(self):
        super().ready()
        

config = NetBoxPluginDummyControllerConfig