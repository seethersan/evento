from django.db import models
from django.contrib.auth.models import AbstractUser
from ubigeo.models import Pais


class User(AbstractUser):
    pais = models.ForeignKey(Pais, verbose_name="País", blank=True, null=True)
    avatar = models.ImageField(verbose_name="Avatar", upload_to='avatar', blank=True, null=True)


