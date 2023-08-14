from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),
    path('membresias/', membresias, name="membresias"),
    path('cliente/', cliente, name="cliente"),
    path('libros/', libros, name="libros"),
    path('autores/', autores, name="autores"),
    path('alumno/', alumno, name="alumno"),
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    path('clienteForm/', clienteForm, name="clienteForm"),
    path('autoresForm/', autoresForm, name="autoresForm"),
    path('librosForm/', librosForm, name="librosForm"),
    path('buscarAutor/', buscarAutor, name="buscarAutor"),
    path('buscar2/', buscar2, name="buscar2"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscarLibros/', buscarLibros, name="buscarLibros"),
    path('updateLibros/<id_libros>/', updateLibros, name="updateLibros"),
    path('deleteLibros/<id_libros>/', deleteLibros, name="deleteLibros"),
    path('updateAutores/<id_autores>/', updateAutores, name="updateAutores"),
    path('deleteAutores/<id_autores>/', deleteAutores, name="deleteAutores"),
    path('editForm/', editarPerfil, name="editForm"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),

]
