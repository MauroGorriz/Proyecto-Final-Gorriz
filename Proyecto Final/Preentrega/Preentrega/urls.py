"""
URL configuration for Preentrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Appentrega.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("sobremi/", sobremi, name = 'sobremi'),
    path("Base/", base , name='Base'),
    path("", inicio,name='Inicio'),
    path("login", inicio_sesion, name='login'),
    path("registro", registro_usuario, name='registro'),
    path("logout", cerrar_sesion , name='logout'),
    path("editar", editar_usuario, name='editar'),

    #Urls para busqueda

    path("busqueda/", busqueda, name='busqueda'),
    path("resultadobusquedacen/", buscar_modelo_bcen, name='resultadobusquedacen'),
    path("resultadobusquedator/", buscar_modelo_btor, name='resultadobusquedator'),
    path("resultadobusquedaeng/", buscar_modelo_beng, name='resultadobusquedaeng'),
    
    #Urls de modelos creados con carga de datos incluida

    path("BombasCentrifugas/",agregar_bcen,name='BombasCentrifugas'),
    path("BombasTornillo/", agregar_btor,name='BombasTornillo'),
    path("BombasEngranaje/", agregar_beng,name='BombasEngranaje'),

    #Urls para actualizar los modelos

    path("ActualizarCentrifuga/<bcen_id>", actualizar_bcen, name='ActualizarCentrifuga'),
    path("ActualizarTornillo/<btor_id>", actualizar_btor, name='ActualizarTornillo'),
    path("ActualizarEngranajes/<beng_id>", actualizar_beng, name='ActualizarEngranajes'),

    #Urls para borrar modelos

    path("BorrarCentrifuga/<bcen_id>", eliminar_bcen, name='BorrarCentrifuga'),
    path("BorrarTornillo/<btor_id>", eliminar_btor, name='BorrarTornillo'),
    path("BorrarEngranajes/<beng_id>", eliminar_beng, name='BorrarEngranajes'), 

]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)