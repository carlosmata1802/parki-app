from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users', blank=True, null=True)
    mobil = models.CharField(max_length=12, default='', help_text='Ingresa un numero no mayor a 12 digitos')
    date_start = models.DateTimeField(editable=False, auto_now=True)
    coin = models.IntegerField(default=0)
    rol = models.CharField(max_length=2, default='PU')
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=64, default='', blank=True)
    address = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=64, default='')
    zip_code = models.CharField(max_length=6, default='')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
