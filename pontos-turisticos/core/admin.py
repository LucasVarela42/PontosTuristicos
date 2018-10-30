from django.contrib import admin

from core.models import DocIdentificacao
from .models import PontoTuristico

admin.site.register(PontoTuristico)
admin.site.register(DocIdentificacao)
