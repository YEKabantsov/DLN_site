from django.conf.urls import url, handler404, handler500
from . import views
from django.views.generic.base import RedirectView
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import urlize as urlize_impl
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url(r'^deklarirovanie$', views.declarate),
    # url(r'^lekarstvenie-preparaty$', views.lp),
    # url(r'^medicinskie-izdeliya$', views.mi),
    # url(r'^bad$', views.bad),
    # url(r'^registraciya$', views.registration),
    # url(r'^sertificaciya$', views.sertification),

    url(r'^lekarstvenie-sredstva$', views.ls),

    url(r'^medicinskie-izdeliya$', views.medprod),
    url(r'^disenfeciruyushie-sredstva$', views.disprod),
    url(r'^sportivnoe-pitanie$', views.sportpit),
    url(r'^cosmeticheskie-sredstva$', views.cosprod),
    url(r'^syryo-bad$', views.rawforbad),
    url(r'^bad$', views.otherbad),
    url(r'^pishhevye-produkty$', views.foodstuffs),
    url(r'^registratsiya-lekarstvennykh-sredstv$', views.regmedecine),
    url(r'^registratsiya-lekarstvennykh-sredstv-rf$', views.regmedecinerf),
    url(r'^vnesenie-izmeneniy$', views.makechanges),
    url(r'^registratsiya-lekarstvennykh-sredstv-eeu$', views.regmedecineeeu),
    url(r'^registratsiya-bad$', views.regbad),
    url(r'^registratsiya-cosmeticheskih-products$', views.regcosmeticproducts),
    url(r'^litsenzirovanie-lekarstvennykh-sredstv$', views.licenseformedicine),
    url(r'^litsenzirovanie-medicinskoi-tehniki$', views.licensemedicaltechnique),
    url(r'^sertifikatsiya-iso$', views.certificationiso),

    url(r'^sertifikatsiya-eeu$', views.certificationeeu),

    url(r'^deklarirovanie-and-sertifikatsiya$', views.declarateandcertificate),
    url(r'^dokumenti$', views.documents),
    url(r'^contact$', views.contact),
    url(r'^reviews$', views.reviews),
    url(r'^message$', views.message, name='message'),

    url(r'^$', views.dln),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
