from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^valid_places.html$', views.valid_places, name='valid_places'),
]