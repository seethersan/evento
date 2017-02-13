from django import forms
from django.contrib.auth import authenticate
from usuarios.models import User


class RegistroForm(forms.ModelForm):
    usuario = forms.CharField(max_length=20)
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    email = forms.CharField(widget=forms.EmailInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        password1_ = self.cleaned_data.get('password1')
        password2_ = self.cleaned_data.get('password2')

        if password1_ != password2_:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return self.cleaned_data

    def save(self):
        usuario = self.cleaned_data.get('usuario')
        nombres = self.cleaned_data.get('nombres')
        apellidos = self.cleaned_data.get('apellidos')
        email = self.cleaned_data.get('email')
        avatar = self.cleaned_data.get('avatar')
        pais = self.cleaned_data.get('pais')
        user = User.objects.create_user(username=usuario, first_name=nombres, last_name=apellidos, email=email)
        password = self.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        perfil = User.objects.create(usuario=user, avatar=avatar, pais=pais)
        perfil.save()

    class Meta:
        model = User
        fields = ('avatar', 'pais')


class LogInForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        usuario_ = self.cleaned_data.get('usuario')
        password_ =self.cleaned_data.get('password')

        usuario_auth = authenticate(username=usuario_, password=password_)
        if not usuario_auth:
            raise forms.ValidationError('Usuario/Password incorrectos')
        else:
            self.cleaned_data['usuario'] = usuario_auth
        return self.cleaned_data