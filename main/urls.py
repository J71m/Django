from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^vaatatootaja/', views.vaatatootaja, name='vaatatootaja'),
  url(r'^lisatootaja/', views.lisatootaja, name='lisatootaja'),
  url(r'^kustutatootaja/', views.kustutatootaja, name='kustutatootaja'),
  url(r'^lisaasutus/', views.lisaasutus, name='lisaasutus')
]
