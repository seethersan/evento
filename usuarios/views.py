from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import UpdateView
from usuarios.forms import RegistroForm, LogInForm
from usuarios.models import User

# Create your views here.


class RegistroView(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm

    def form_valid(self, form):
        form.save()
        usuario = authenticate(username=form.cleaned_data['usuario'], password=form.cleaned_data['password1'])
        login(self.request, usuario)
        return redirect('home')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class Login(FormView):
    template_name = 'login.html'
    form_class = LogInForm

    def form_valid(self, form):
        usuario = form.cleaned_data['usuario']
        login(self.request, usuario)
        return redirect('home')


class Perfil(UpdateView):
    template_name = 'perfil.html'
    model = User
    fields = ('first_name', 'last_name', 'email', 'avatar', 'pais')

    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

