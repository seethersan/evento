from django.contrib import admin
from ubigeo.models import Pais

# Register your models here.

class PaisAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'ubicacion',)
    search_fields = ('codigo', 'nombre',)

admin.site.register(Pais, PaisAdmin)