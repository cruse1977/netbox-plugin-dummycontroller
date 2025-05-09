# netbox-plugin-helloworld

# about

This a simple netbox helloworld type plugin to demonstrate a plugin without models

# install

```
git clone https://github.com/cruse1977/netbox-plugin-helloworld.git
source /opt/netbox/venv/bin/activate
python3 setup.py install

edit /opt/netbox/netbox/netbox/configuration.py and add 'netbox_plugin_helloworld' to PLUGINS = []
restart netbox,netbox-rq
```

# usage

```
go to: <NETBOX_URL>/api/plugins/plugin-helloworld/say-hello/

response should be:

["this", "is", "hello", "world"]

```
