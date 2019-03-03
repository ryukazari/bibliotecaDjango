from django.shortcuts import render, redirect
from .models import *
from .forms import UsuarioForm

from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# CRUD - vistas basadas en Clases

class CrearUsuario(CreateView):
    model = Usuario
    form_class =  UsuarioForm
    template_name = 'aplicacion/crearUsuario.html'
    success_url = reverse_lazy('index')

class ListUsuario(ListView):
    model = Usuario
    template_name = 'aplicacion/listarUsuarios.html'

class UpdateUsuario(UpdateView):
    model = Usuario
    form_class =  UsuarioForm
    template_name = 'aplicacion/crearUsuario.html'
    success_url = reverse_lazy('index')

class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'aplicacion/eliminarUsuario.html'
    success_url = reverse_lazy('index')




# CRUD - Vistas basadas en Funciones
def agregarUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()

    return render(request,'aplicacion/crearUsuario.html',{'form': form})

def home(request):
    return render(request, 'index.html')

def listarUsuario(request):
    usuario = Usuario.objects.all();
    context = {'usuario':usuario}
    return render (request, 'aplicacion/listarUsuario.html',context)

def modificarUsuario(request, id):
    usuario = Usuario.objects.get(_dni = id)
    if request.method == 'GET':
        form = UsuarioForm(instance = usuario)
    else:
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'aplicacion/crearUsuario.html',{'form':form})

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(_dni=id)
    if request.method == 'POST' :
        usuario.delete()
        return redirect('index')
    return render(request,'aplicacion/eliminarUsuario.html',{'usuario':usuario})
