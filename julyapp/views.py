from django.shortcuts import render
from django.http import HttpResponse
from.serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
# Create your views here.

class studentlist(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Demomodel.all()
    serializer_class=studentserlaizer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

"""def demo(request):
    return HttpResponse("this is my 1st project")"""
    
