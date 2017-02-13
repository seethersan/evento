from django.http import JsonResponse
from django.views.generic import CreateView
from django.views.generic import DetailView
from evento.models import Evento

# Create your views here.
from ubigeo.models import Pais
from usuarios.models import User


class DetalleEvento(DetailView):
    template_name = 'detalle.html'
    model = Evento


class CrearEvento(CreateView):
    template_name = 'crearevento.html'
    model = Evento
    fields = ['nombre', 'descripcion', 'direccion', 'longitud', 'latitud', 'pais']

    def post(self, request):
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        direccion = request.POST['direccion']
        longitud = request.POST['longitud']
        latitud = request.POST['latitud']
        pais = int(request.POST['pais'])
        pais = Pais.objects.get(id=pais)
        usuario = request.POST['usuario']
        usuario = User.objects.get(username=usuario)
        evento = Evento(nombre=nombre,descripcion=descripcion,direccion=direccion,latitud=float(latitud),longitud=float(longitud),pais=pais,usuario = usuario)
        evento.save()
        return JsonResponse({"ok": "ok"})