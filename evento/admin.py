from django.contrib import admin
from evento.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'latitud', 'longitud',)
    search_fields = ('nombre', 'direccion',)


admin.site.register(Evento, EventoAdmin)