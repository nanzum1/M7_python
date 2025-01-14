from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio

# Ver Laboratorios
def ver_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    context = {
        'laboratorios': laboratorios
    }
    return render(request, 'ver_laboratorios.html', context)

# Agregar Laboratorio
def agregar_laboratorio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        laboratorio = Laboratorio(nombre=nombre)
        laboratorio.save()
        return redirect('laboratorio-list')  # Redirige a la lista de laboratorios
    return render(request, 'crear_laboratorio.html')

# Vista para editar un laboratorio
def editar_laboratorio(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == 'POST':
        laboratorio.nombre = request.POST['nombre']
        laboratorio.ciudad = request.POST['ciudad']
        laboratorio.pais = request.POST['pais']
        laboratorio.save()
        return redirect('laboratorio-list')
    return render(request, 'editar_laboratorio.html', {'laboratorio': laboratorio})

# Vista para eliminar un laboratorio
def eliminar_laboratorio(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
        # Si el método es POST, se procede a eliminar
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio-list')  # Redirige a la lista de laboratorios después de eliminar

    # Si no es POST, se muestra la confirmación
    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})
