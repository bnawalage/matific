
from django.conf.urls import url

from demo.fbv_demo.views import save_venue, get_venue

urlpatterns = [
    url(r'^save_venue', save_venue, name='save_venue'),
    url(r'^get_venue', get_venue, name='get_venue'),
]
