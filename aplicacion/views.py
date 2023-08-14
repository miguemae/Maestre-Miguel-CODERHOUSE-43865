from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *
from .models import *


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def alumno(request):
    return render(request, "aplicacion/alumno.html")

def index(request):
    return render(request, "aplicacion/base.html")

def membresias(request):
    ctx = {"membresias": Membresias.objects.all()}
    return render(request, "aplicacion/membresias.html", ctx)

@login_required
def libros(request):
    ctx = {"libros": Libros.objects.all()}
    return render(request, "aplicacion/libros.html", ctx)

@login_required
def cliente(request):
    ctx = {"cliente": Cliente.objects.all()}
    return render(request, "aplicacion/cliente.html", ctx)

@login_required
def autores(request):
    ctx = {"autores": Autores.objects.all()}
    return render(request, "aplicacion/autores.html", ctx)

@login_required
def clienteForm(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], dni=request.POST['dni'], email=request.POST['email'], tipo=request.POST['tipo'])
        cliente.save()
        return HttpResponse("Hemos registrado tus datos!")
    return render(request, "aplicacion/clienteForm.html")

@login_required
def autoresForm(request):
    if request.method == "POST":
        autores = Autores(nombre=request.POST['nombre'], apellido=request.POST['apellido'])
        autores.save()
        return HttpResponse("Hemos registrado tus datos!")
    else:
        autores_Form = AutoresForm()
        return render(request, "aplicacion/autoresForm.html", {"form":autores_Form})
    
@login_required
def librosForm(request):
    if request.method == "POST":
        libros = Libros(nombre=request.POST['nombre'], autor=request.POST['autor'], anio=request.POST['anio'], editorial=request.POST['editorial'])
        libros.save()
        return HttpResponse("Hemos registrado tus datos!")
    else:
        libros_Form = LibrosForm()
        return render(request, "aplicacion/librosForm.html", {"form":libros_Form})

@login_required
def buscarAutor(request):
    return render(request, "aplicacion/buscarAutor.html")

@login_required
def buscar2(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        apellido = Autores.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadoAutores.html", 
                      {"nombre":nombre, "apellido":apellido})
    return HttpResponse("No se ingresaron datos para la busqueda")

@login_required   
def buscarLibros(request):
    return render(request, "aplicacion/buscarLibros.html")

@login_required
def buscar3(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        autor = Libros.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadoLibros.html", 
                      {"nombre":nombre, "autor":autor})
    return HttpResponse("No se ingresaron datos para la busqueda")

@login_required
def updateLibros(request, id_libros):
    libros = Libros.objects.get(id=id_libros)
    if request.method == "POST":
        miForm = LibrosForm(request.POST)
        if miForm.is_valid():
            libros.nombre = miForm.cleaned_data.get('nombre')
            libros.autor = miForm.cleaned_data.get('autor')
            libros.anio = miForm.cleaned_data.get('anio')
            libros.editorial = miForm.cleaned_data.get('editorial')
            libros.save()
            return redirect(reverse_lazy('libros'))
    else:
        mi_Form = LibrosForm(initial={'nombre':libros.nombre,
                                     'autor':libros.autor,
                                     'anio':libros.anio,
                                     'editorial':libros.editorial})
    return render(request, "aplicacion/librosForm.html", {"form": mi_Form})

@login_required
def deleteLibros(request, id_libros):
    libros = Libros.objects.get(id=id_libros)
    libros.delete()
    return redirect(reverse_lazy('libros'))

@login_required
def updateAutores(request, id_autores):
    autores = Autores.objects.get(id=id_autores)
    if request.method == "POST":
        miForm = AutoresForm(request.POST)
        if miForm.is_valid():
            autores.nombre = miForm.cleaned_data.get('nombre')
            autores.apellido = miForm.cleaned_data.get('apellido')
            autores.save()
            return redirect(reverse_lazy('autores'))
    else:
        mi_Form = AutoresForm(initial={'nombre':autores.nombre,
                                     'apellido':autores.apellido,})
    return render(request, "aplicacion/autoresForm.html", {"form": mi_Form})

@login_required
def deleteAutores(request, id_autores):
    autores = Autores.objects.get(id=id_autores)
    autores.delete()
    return redirect(reverse_lazy('autores'))

#_________ creacion de los login, Logout, Registro#


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
               
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid(): #Si pasa la validacion de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})
    else:
        form = RegistroUsuariosForm()

    return render(request, "aplicacion/registro.html", {"form": form})

#____Administración de users_____#

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editForm.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editForm.html", {'form': form, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    usuario = request.user
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen


            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})