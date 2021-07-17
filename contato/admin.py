from django.contrib import admin
from .models import Contato, Category


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone', 'category']
    list_display_links = ['name', 'last_name']


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Category)
