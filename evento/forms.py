from django import forms
from address.forms import AddressField


class EventoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.Textarea()
    direccion = AddressField()