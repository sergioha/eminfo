from django.contrib import admin
from apps.usuarios.models import *

# Register your models here.
admin.site.register(Login)
admin.site.register(Rol)
admin.site.register(Usuario)