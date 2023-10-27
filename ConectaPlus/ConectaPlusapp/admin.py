from django.contrib import admin

# Register your models here.
#superuser: host
#senha: 123
from .models import Perfil, Projeto, Voluntario

class ListandoPerfil(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links =("id", "name")
    search_fields = ("name",)

admin.site.register(Perfil, ListandoPerfil)


class ListandoProjeto(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links =("id", "name")
    search_fields = ("name",)

admin.site.register(Projeto, ListandoProjeto)

class ListandoVoluntario(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links =("id", "name")
    search_fields = ("name",)

admin.site.register(Voluntario)