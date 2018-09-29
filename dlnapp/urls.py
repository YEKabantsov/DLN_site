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

    url(r'^lekarstvenie-sredstva$', views.ls),

    url(r'^medical-products$', views.medprod),
    url(r'^disinfecting-products$', views.disprod),
    url(r'^sport-nutrition$', views.sportpit),
    url(r'^cosmetic-products$', views.cosprod),
    url(r'^raw-for-bad$', views.rawforbad),
    url(r'^other-bad$', views.otherbad),
    url(r'^foodstuffs$', views.foodstuffs),
    url(r'^register-medicine$', views.regmedecine),
    url(r'^register-medicine-rf$', views.regmedecinerf),
    url(r'^make-changes$', views.makechanges),
    url(r'^register-medicine-eeu$', views.regmedecineeeu),
    url(r'^register-bad$', views.regbad),
    url(r'^register-cosmetic-products$', views.regcosmeticproducts),
    url(r'^license-for-medicine$', views.licenseformedicine),
    url(r'^license-medical-technique$', views.licensemedicaltechnique),
    url(r'^certification-iso$', views.certificationiso),

    url(r'^certification-eeu$', views.certificationeeu),

    url(r'^declarate-and-certificate$', views.declarateandcertificate),
    url(r'^documents$', views.documents),

    url(r'^$', views.dln),
]