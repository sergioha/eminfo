from django.contrib import admin

from apps.eventos.models import Evento
#from refugio.admin_site import custom_admin_site

# Register your models here.

admin.site.register(Evento)