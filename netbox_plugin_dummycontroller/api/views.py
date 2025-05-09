import copy
from . import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ViewSet
from dcim.models import Device


class ControllerView(ViewSet):
    ''' view for the main controller '''

    data = [
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
        },
        {
            "name": "pdu02",
            "model": "APC5958",
            "total_load": "11.1A",
            "ports": {
                "outlet3": {
                    "type": "C13",
                    "rating": 10,
                    "current": 4.3
                },
                "outlet4": {
                    "type": "C13",
                    "rating": 10,
                    "current": 4.3
                }
            }
        }
    ]

    permission_required = ("dcim.view_site")
    queryset = Device.objects.none()
    serializer_class = serializers.HelloWorldDummySerializer()

    ''' returns the full data list - the port data '''
    def list(self, request, **kwargs):
        if 'name' not in request.GET:
            working_data = copy.deepcopy(self.data)
            for pos, item in enumerate(working_data):
                del working_data[pos]["ports"]

            return JsonResponse(
                    working_data, status=200, safe=False
            )
        else:
            for pos, val in enumerate(self.data):
                if val["name"] == request.GET['name']:
                    return JsonResponse(
                        val, status=200, safe=False
                    )
            return JsonResponse(
                    dict(error="no data found"), status=404, safe=False
            )
