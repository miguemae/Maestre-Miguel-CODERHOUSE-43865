from django.contrib import admin
from .models import Libros, Cliente, Membresias, Autores, Avatar


# Register your models here.
admin.site.register(Libros)
admin.site.register(Cliente)
admin.site.register(Membresias)
admin.site.register(Autores)
admin.site.register(Avatar)