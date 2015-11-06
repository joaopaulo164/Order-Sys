from django.conf.urls import include, url
from django.contrib import admin

from tastypie.api import Api
from manager.resources import ClienteResource

v1_api = Api(api_name='v1')
v1_api.register(ClienteResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'OrderSys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
]
