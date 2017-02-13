from django.conf.urls import url
from evento import views

urlpatterns = [
    url(r'^detalle/(?P<pk>\d+)/?$', views.DetalleEvento.as_view(), name='detalle'),
    url(r'crear/?$', views.CrearEvento.as_view(), name='crearevento'),
]