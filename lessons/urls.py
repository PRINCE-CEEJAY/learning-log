from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_lesson, name='create_lesson'),
    path('', views.get_lessons, name='get_lessons'),
    path('<int:id>', views.get_lesson, name='get_lesson'), #implement template later
    path('<int:id>/', views.lesson_update, name='lesson_update'),
    path('<int:id>/', views.lesson_delete, name='lesson_delete'),
]