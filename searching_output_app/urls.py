from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^valid_places$', views.valid_places, name='valid_places'),
    url(r'^place/(?P<pk>\d+)/$', views.place_details, name='place_details'),
]