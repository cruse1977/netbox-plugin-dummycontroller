from rest_framework import serializers
from dcim.models import Device

class HelloWorldDummySerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id", "name")

