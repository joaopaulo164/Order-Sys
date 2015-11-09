__author__ = 'joao'

from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from manager.models import Cliente, Funcionario, Historico, Servico


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }


class ClienteResource(ModelResource):

    class Meta:
        queryset = Cliente.objects.all()
        resource_name = 'cliente'
        authorization = Authorization()
        filtering = {
            'nome': ALL,
            #'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }

class FuncionarioResource(ModelResource):

    class Meta:
        queryset = Funcionario.objects.all()
        resource_name = 'funcionario'
        authorization = Authorization()
        filtering = {
            'nome': ALL,
            #'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }

class ServicoResource(ModelResource):

    class Meta:
        queryset = Servico.objects.all()
        resource_name = 'servico'
        authorization = Authorization()
        filtering = {
            'nome': ALL,
            #'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }

class HistoricoResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente', full=True)
    funcionario = fields.ForeignKey(FuncionarioResource, 'funcionario', full=True)
    servicos = fields.ToManyField(ServicoResource, 'servico', full=True, null=True)
    # profile = fields.ToOneField('resources.UserProfileResource', attribute = 'userprofile', related_name='user', full=True, null=True)

    class Meta:
        queryset = Historico.objects.all()
        resource_name = 'historico'
        authorization = Authorization()
        filtering = {
            'cliente': ALL_WITH_RELATIONS,
            #'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }