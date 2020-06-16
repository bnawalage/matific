
from django.conf.urls import url

from demo.cbv_demo.views import GeneralViewSet

urlpatterns = [
    url(r'^/(?P<model>\w+)', GeneralViewSet.as_view({'get': 'list'})),
    url(r'^/(?P<model>\w+)/(?P<pk>[0-9]+)$', GeneralViewSet.as_view({'get': 'list', 'put': 'create'}))
]