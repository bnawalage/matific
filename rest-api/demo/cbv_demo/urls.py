
from django.conf.urls import url

from demo.cbv_demo import views

urlpatterns = [
    url(r'^api/venues$', views.get_venues),
    url(r'^api/venues/(?P<pk>[0-9]+)$', views.venue),
]