from django.shortcuts import render
from .models import Tournament, Team, Player

# Create your views here.
def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'football_app/tournament_list.html', {'tournaments': tournaments})


def team_detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'football_app/team_detail.html', {'team': team, 'players': players})

