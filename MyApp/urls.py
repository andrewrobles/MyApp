from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/do/', views.do, name='do'),
    path('<int:id>/undo/', views.undo, name='undo'),
    path('<int:id>/undo/', views.undo, name='undo'),
    path('create/<str:text>/', views.create, name='create'),
]