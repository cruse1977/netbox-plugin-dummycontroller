# netbox-plugin-helloworld

# about

This a simple netbox plugin to mimic a controller for a power monitoring system, with list and get functionality

# install

```
git clone https://github.com/cruse1977/netbox-plugin-dummycontroller.git
source /opt/netbox/venv/bin/activate
python3 setup.py install

edit /opt/netbox/netbox/netbox/configuration.py and add 'netbox_plugin_dummycontroller' to PLUGINS = []
restart netbox,netbox-rq
```

# usage

go to: <NETBOX_URL>/api/plugins/dummycontroller/pdus/

response should be:

```
[
  {
    "name": "pdu01",
    "model": "APC5978",
    "total_load": "13.1A"
  },
  {
    "name": "pdu02",
    "model": "APC5958",
    "total_load": "11.1A"
  }
]
```

or call an individual by name:

<NETBOX_URL>/api/plugins/dummycontroller/pdus/?name=pdu01

```
{
  "name": "pdu01",
  "model": "APC5978",
  "total_load": "13.1A",
  "ports": {
    "outlet1": {
      "type": "C13",
      "rating": 10,
      "current": 4.3
    },
    "outlet2": {
      "type": "C13",
      "rating": 10,
      "current": 4.3
    }
  }
}
```
