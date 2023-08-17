
# Register your models here.
from django.contrib import admin

from criticos.models import Critico, Restaurante

admin.site.register(Critico)
admin.site.register(Restaurante)