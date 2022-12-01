from django.contrib import admin

# Register your models here.

from .models import Categorie, Menu

admin.site.register(Categorie)
admin.site.register(Menu)


