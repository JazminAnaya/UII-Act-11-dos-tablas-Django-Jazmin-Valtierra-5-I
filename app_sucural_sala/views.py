from django.shortcuts import render, get_object_or_404, redirect
from .models import Sucursal
from .forms import SucursalForm

def listar_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'listar_sucursales.html', {'sucursales': sucursales})

def detalle_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id_sucursal=sucursal_id)
    return render(request, 'detalle_sucursal.html', {'sucursal': sucursal})

def crear_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_sucural_sala:listar_sucursales')
    else:
        form = SucursalForm()
    return render(request, 'formulario_sucursal.html', {'form': form, 'titulo': 'Crear Sucursal'})

def editar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id_sucursal=sucursal_id)
    if request.method == 'POST':
        form = SucursalForm(request.POST, request.FILES, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('app_sucural_sala:detalle_sucursal', sucursal_id=sucursal.id_sucursal)
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'formulario_sucursal.html', {'form': form, 'titulo': 'Editar Sucursal'})

def borrar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id_sucursal=sucursal_id)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('app_sucural_sala:listar_sucursales')
    return render(request, 'confirmar_borrar.html', {'sucursal': sucursal})