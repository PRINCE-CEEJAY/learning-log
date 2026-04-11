from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('create/', views.lesson_list_create_view, name='create_lesson'),
    path('', views.get_lessons, name='get_lessons'),
    path('update/<int:id>/', views.lesson_update, name='lesson_update'),
    path('detail/<int:id>/', views.get_details, name='lesson_detail'),
    path('delete/<int:id>/', views.lesson_delete, name='lesson_delete'),
]