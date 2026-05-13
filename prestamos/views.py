from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Prestamo
from .serializer import PrestamoSerializer
from .forms import PrestamoForm


# CRUD completo de préstamos para la API REST.
class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

# Vistas HTML para administrar préstamos desde plantillas.
def prestamo_list(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/list.html', {'prestamos': prestamos})

def prestamo_create(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prestamo_list')
    else:
        form = PrestamoForm()
    return render(request, 'prestamos/form.html', {'form':form})

def prestamo_update(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('prestamo_list')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request,'prestamos/form.html', {'form': form})

def prestamo_delete(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('prestamo_list')
    return render(request, 'prestamos/delete.html', {'prestamo': prestamo})
