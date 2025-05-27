from django.urls import path
from app import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index,name='inicio'),
    path('Iniciar Sesion', views.iniciar, name='Iniciar Sesion'),
    path('Registrarse', views.registrarse, name='Registrarse'),
    path('Comestibles', views.comestibles, name='comestibles'),
    path('Productos', views.productos, name='productos'),
    path('Iniciobd', views.empieza, name='empieza'),
    path('Productos/Crear', views.crear, name='crear'),
    path('Productos/Editar', views.editar, name='editar'),
    path('registrar_producto', views.registrar_elproducto, name='registrar_producto'),

    path('productos/listar', views.listar_elproducto, name='listar_elproducto'),
    path('api/productos/', views.productos_json, name='productos_json'),


    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
