from django.contrib import admin

# Register your models here.

from .models import Perfil, Projeto

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
