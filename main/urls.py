from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^vaatatootaja/', views.vaatatootaja, name='vaatatootaja'),
  url(r'^lisatootaja/', views.lisatootaja, name='lisatootaja'),
  url(r'^kustutatootaja/', views.kustutatootaja, name='kustutatootaja'),
  url(r'^lisaasutus/', views.lisaasutus, name='lisaasutus'),
  url(r'^vaataasutus/', views.vaataasutus, name='vaataasutus'),
  url(r'^muudaasutusnimi/', views.muudaasutusnimi, name='muudaasutusnimi'),
  url(r'^muudaasutus/', views.muudaasutus, name='muudaasutus'),
  url(r'^kustutaasutus/', views.kustutaasutus, name='kustutaasutus')
]
