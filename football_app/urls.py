from django.urls import path
from . import views

urlpatterns = [
    path('tornaments/', views.tournament_list, name='tournament'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail')
]