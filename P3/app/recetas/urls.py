# recetas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<pk>', views.detalle, name='detalle'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('post_new/', views.post_new, name="post_new"),
    path('post_edit/<pk>', views.post_edit, name="post_edit"),
    path('post_delete/<pk>', views.post_delete, name="post_delete"),

]