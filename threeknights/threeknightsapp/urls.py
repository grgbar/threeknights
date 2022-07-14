from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercise/<int:exercise_id>', views.exercise_by_id, name='exercise_by_id'),
]