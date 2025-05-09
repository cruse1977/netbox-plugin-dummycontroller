from extras.plugins import PluginConfig
from .version import __version__

class NetBoxPluginHelloWorldConfig(PluginConfig):
    name = 'netbox_plugin_helloworld'
    verbose_name = 'NetBox Plugin HelloWorld'
    description = ''
    version = __version__
    base_url = 'plugin-helloworld'
    min_version = '3.5.0'
    max_version = '3.6.99'

    def ready(self):
        super().ready()
        

config = NetBoxPluginHelloWorldConfig