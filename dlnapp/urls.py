from django.conf.urls import url, handler404, handler500
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^deklarirovanie$', views.declarate),
    url(r'^lekarstvenie-preparaty$', views.lp),
    url(r'^medicinskie-izdeliya$', views.mi),
    url(r'^bad$', views.bad),
    url(r'^registraciya$', views.registration),
    url(r'^sertificaciya$', views.sertification),
    url(r'^$', views.dln),
]