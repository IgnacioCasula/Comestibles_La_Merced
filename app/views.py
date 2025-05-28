from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import elproducto
from .forms import elproductoForm
from .models import producto
from .forms import ProductoForm


# Create your views here.
def index(request):
    return render(request, 'inicio.html')
def iniciar(request):
    return render(request, 'iniciar sesion.html')
def registrarse(request):
    return render(request, 'Registrarse.html')
def comestibles(request):
    return render(request, 'comestibles.html')
def productos (request):
    productos_list=producto.objects.all()
    return render(request, 'Productos/index.html', {'productos': productos_list})
def empieza (request):
    return render(request, 'empieza.html')
def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'Productos/crear.html', {'formulario': formulario})
def editar(request, id):
    producto_obj = get_object_or_404(producto, id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto_obj)
    if formulario.is_valid() and request.method == "POST":
        formulario.save()
        return redirect('productos')  
    return render(request, 'Productos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    producto_obj = get_object_or_404(producto, id=id)
    producto_obj.delete()
    return redirect('productos')






def registrar_elproducto(request):
    form = elproductoForm()

    if request.method == 'POST':
        form = elproductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_elproducto')
        
    return render(request, 'registrar_producto.html', {'form': form})

def listar_elproducto(request):
    return render(request, 'TablasProductos.html')

def productos_json(request):
    productos = elproducto.objects.all().values('idprod', 'nombre', 'precio', 'stock')
    return JsonResponse({'data': list(productos)})

def editar_elproducto(request, id):
    producto = get_object_or_404(elproducto, pk=id)
    if request.method == 'POST':
        form = elproductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_elproducto')
    else:
        form = elproductoForm(instance=producto)
    return render(request, 'editar.html', {'form': form, 'producto': producto})

def eliminar_elproducto(request, id):
    producto = get_object_or_404(elproducto, pk=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_elproducto')
    return render(request, 'eliminar.html', {'producto': producto})






