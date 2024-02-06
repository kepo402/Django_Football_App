from django.urls import path
from . import views
from .views import placeholder_view

urlpatterns = [

    path('', placeholder_view, name='placeholder'),
    path('tournaments/', views.tournament_list, name='tournament'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
 ]