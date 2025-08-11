from django.urls import path
from . import views

app_name= 'articles'

urlpatterns = [
    path('monsters/', views.monster_list, name='monster_list'),
    path('monsters/<int:pk>/', views.monster_detail, name='monster_detail'),
    path('observations/', views.observation_list, name='observation_list'),
    path('observations/create/', views.create_observation, name='create_observation'),
    path('observations/<slug:slug>/', views.observation_detail, name='observation_detail'),
    path('observations/<slug:slug>/edit/', views.edit_observation, name='edit_observation'),
    path('observations/<slug:slug>/delete/', views.delete_observation, name='delete_observation'),
]