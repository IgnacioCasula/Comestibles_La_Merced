from django.urls import path #path se usa para definir rutas.
from app import views #views trae las funciones que están en views.py.

from django.conf import settings #settings y static sirven para mostrar imágenes u otros archivos cargados por los usuarios.
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index,name='inicio'), #Esto significa que si el usuario entra al sitio principal, se muestra la función index.
    path('Iniciar Sesion', views.iniciar, name='Iniciar Sesion'), #Estas rutas muestran las páginas para iniciar sesión o registrarse.
    path('Registrarse', views.registrarse, name='Registrarse'),
    path('Comestibles', views.comestibles, name='comestibles'),  #Estas rutas muestran otras páginas del sitio.
    path('Productos', views.productos, name='productos'),
    path('Iniciobd', views.empieza, name='empieza'),
    path('Productos/Crear', views.crear, name='crear'), #Ignorar
    path('Productos/Editar/<int:id>', views.editar, name='editar'), #Ignorar


    path('registrar_producto', views.registrar_elproducto, name='registrar_producto'), #Estas sirven para registrar, listar, editar o eliminar un producto.
    path('productos/listar', views.listar_elproducto, name='listar_elproducto'),
    path('api/productos/', views.productos_json, name='productos_json'),
    path('editar_producto/<int:id>', views.editar_elproducto, name='editar_elproducto'), #Devuelve los productos en formato JSON. Sirve para usar los datos desde JavaScript u otra app.
    path('eliminar_producto/<int:id>', views.eliminar_elproducto, name='eliminar_elproducto'),
    




    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Esto se usa para poder mostrar imágenes o archivos que se cargan desde la página.
