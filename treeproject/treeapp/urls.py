from django.urls import path
from treeapp import views as treeapp


app_name = 'treeapp'

urlpatterns = [
    path('', treeapp.treeview, name='tree'),
    path('<int:pk>/', treeapp.nodeview, name='node'),

]
