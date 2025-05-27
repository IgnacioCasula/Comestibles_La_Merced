from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import elproducto
from .forms import elproductoForm

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
    return render(request, 'Productos/index.html')
def empieza (request):
    return render(request, 'empieza.html')
def crear(request):
    return render(request, 'Productos/crear.html')
def editar(request):
    return render(request, 'Productos/editar.html')

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


    