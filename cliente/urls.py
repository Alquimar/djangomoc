from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cliente, name='cliente_principal'),
    url(r'^novo/$', views.create, name='cliente_create'),
    url(r'^(?P<pk>\d+)/$', views.cliente_update, name='cliente_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='cliente_delete'),
]
