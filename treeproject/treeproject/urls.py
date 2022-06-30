from django.contrib import admin
from django.urls import path, include
from treeapp import views as treeapp



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('treeapp.urls', namespace='tree')),
]

