from django.shortcuts import render, redirect, get_object_or_404  #get_object_or_404: busca un objeto en la base de datos y, si no lo encuentra, muestra un error 404.
from django.http import JsonResponse   #se usa para devolver datos en formato JSON 
from .models import elproducto  #importan modelos  y sus formularios asociados
from .forms import elproductoForm
from .models import producto
from .forms import ProductoForm

# Create your views here.
def index(request):   #index, iniciar, registrarse, comestibles, empieza: simplemente renderizan plantillas HTML.
    return render(request, 'inicio.html')
def iniciar(request):
    return render(request, 'iniciar sesion.html')
def registrarse(request):
    return render(request, 'Registrarse.html')
def comestibles(request):
    return render(request, 'comestibles.html')
def empieza (request):
    return render(request, 'empieza.html')

def productos (request):
    productos_list=producto.objects.all()   #Busca todos los objetos del modelo producto y los guarda en la variable productos_list.
    return render(request, 'Productos/index.html', {'productos': productos_list}) #Después, manda esa lista a la plantilla Productos/index.html para que los muestre en pantalla.
def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None) #Si la página se abrió por primera vez, muestra un formulario vacío
    if formulario.is_valid(): #Si el usuario completó el formulario y lo envió, se valida.
        formulario.save() #Si es válido, lo guarda en la base de datos 
        return redirect('productos') #y redirige a la vista productos.
    return render(request, 'Productos/crear.html', {'formulario': formulario}) #Si no es válido o es la primera vez, vuelve a mostrar el formulario.
def editar(request, id):
    producto_obj = get_object_or_404(producto, id=id) #Busca un producto por su ID.
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto_obj) #Carga el formulario con los datos de ese producto.
    if formulario.is_valid() and request.method == "POST": #Si el formulario fue enviado y es válido
        formulario.save() #guarda los cambios
        return redirect('productos') #y redirige a la vista productos.
    return render(request, 'Productos/editar.html', {'formulario': formulario}) #Si no, muestra el formulario para editar.
def eliminar(request, id):
    producto_obj = get_object_or_404(producto, id=id) #Busca un producto por su ID.
    producto_obj.delete() #Lo elimina directamente de la base de datos.
    return redirect('productos') #y redirige a la vista productos.

def registrar_elproducto(request):
    form = elproductoForm() #Crea un formulario vacío basado en el modelo elproducto.
    if request.method == 'POST': #Verifica si el usuario envió el formulario
        form = elproductoForm(request.POST) #Carga el formulario con los datos enviados.
        if form.is_valid(): #Si los datos son válidos
            form.save() #guarda el producto en la base de datos.
            return redirect('listar_elproducto') #Después redirige a la página que muestra la tabla de productos 
    return render(request, 'registrar_producto.html', {'form': form}) #Si el formulario no se envió aún o es inválido, se vuelve a mostrar el mismo formulario
def listar_elproducto(request):
    return render(request, 'TablasProductos.html') #Muestra una tabla HTML con los productos
def productos_json(request):
    productos = elproducto.objects.all().values('idprod', 'nombre', 'precio', 'stock') #Busca todos los productos del modelo elproducto y extrae siertos campos.
    return JsonResponse({'data': list(productos)}) #Los convierte a lista y los devuelve como JSON.
def editar_elproducto(request, id):
    producto = get_object_or_404(elproducto, pk=id) #Busca el producto con el ID, si no lo encuentra, muestra error 404.
    if request.method == 'POST': #Si el usuario ya envió el formulario
        form = elproductoForm(request.POST, instance=producto) #Crea el formulario cargado con los datos nuevos y lo vincula al producto original.
        if form.is_valid(): #Si los datos son válidos
            form.save() #los guarda en la base de datos
            return redirect('listar_elproducto') #y redirige a la tabla.
    else: #Si todavía no se envió nada
        form = elproductoForm(instance=producto) #carga el formulario con los datos actuales del producto para que el usuario pueda modificarlos.
    return render(request, 'editar.html', {'form': form, 'producto': producto}) #Muestra la plantilla HTML con el formulario de edición.
def eliminar_elproducto(request, id):
    producto = get_object_or_404(elproducto, pk=id) #Busca el producto por ID
    if request.method == 'POST': #Si el usuario ya confirmó 
        producto.delete() #Elimina el producto
        return redirect('listar_elproducto') #y vuelve a la tabla.
    return render(request, 'eliminar.html', {'producto': producto}) #Si todavía no se confirmó, muestra la página eliminar.html para preguntar al usuario si está seguro.



