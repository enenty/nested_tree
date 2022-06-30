from django.contrib import admin
from .models import Tree


class TreeAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']

admin.site.register(Tree, TreeAdmin)
