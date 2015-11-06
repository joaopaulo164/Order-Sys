__author__ = 'joao'

from tastypie.resources import ModelResource
from manager.models import Cliente


class ClienteResource(ModelResource):
    class Meta:
        queryset = Cliente.objects.all()
        allowed_methods = ['get']