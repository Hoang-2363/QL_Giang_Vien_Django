from django.urls import path
from .import views

urlpatterns = [
    path('', views.trangchu, name='trangchu'),
    path('khoa/', views.index, name='index'),
    path('khoa/<int:id>', views.view_student, name='view_student'),
    path('khoa/add/', views.add, name='add'),
    path('khoa/edit/<int:id>/', views.edit, name='edit'),
    path('khoa/delete/<int:id>/', views.delete, name='delete'),
]