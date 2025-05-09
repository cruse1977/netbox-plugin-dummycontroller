from . import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ViewSet
from dcim.models import Device

class SayHelloView(ViewSet):
    ''' says hello  '''
    permission_required = ("dcim.view_site")
    queryset = Device.objects.none()
    serializer_class = serializers.HelloWorldDummySerializer()

    def list(self,request, **kwargs):
        hello_msg = [
            'this',
            'is',
            'hello',
            'world'
        ]

        return JsonResponse(
                hello_msg, status=200, safe=False
        )