from django.contrib import admin

from comentarios.actions import reprova_comentarios, aprova_comentarios
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]


admin.site.register(Comentario, ComentarioAdmin)
