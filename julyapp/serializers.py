from rest_framework import serializers
from julyapp.models import Demomodel

class studentserlaizer(serializers.ModelSerializer):
    class meta:
        model=Demomodel
        fields="__all__"
    