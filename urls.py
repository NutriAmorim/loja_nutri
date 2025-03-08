from django.contrib import admin
from django.urls import path, include
from loja_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.boas_vindas, name='boas_vindas'),  # Página inicial
    path('receitas_medicinais/', views.receitas_medicinais, name='receitas_medicinais'),
    path('pesquisas_cientificas/', views.pesquisas_cientificas, name='pesquisas_cientificas'),
    path('quem_sou_eu/', views.quem_sou_eu, name='quem_sou_eu'),
    path('quem_somos_nos/', views.quem_somos_nos, name='quem_somos_nos'),
]