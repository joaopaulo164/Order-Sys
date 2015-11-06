__author__ = 'joao'

from django.conf.urls import include, patterns
from tastypie.api import Api
from manager.resources import ClienteResource

v1_api = Api(api_name='v1')
v1_api.register(ClienteResource())

urlpatterns = patterns('',
  # ...more URLconf bits here...
  # Then add:
  (r'^api/', include(v1_api.urls)),
)