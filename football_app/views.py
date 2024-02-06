from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Tournament, Match, Player, Team
from django.http import HttpResponse

def placeholder_view(request):
    return HttpResponse("Welcome to Football Tracker!")

def tournament_list(request):
    tournaments = Tournament.objects.all()

    # Fetch matches for each tournament
    matches_by_tournament = {}
    for tournament in tournaments:
        matches = Match.objects.filter(tournament=tournament)
        matches_by_tournament[tournament] = matches

    # Calculate standings for each team
    standings = Team.objects.annotate(matches_played=Count('player__match')).order_by('-matches_played')

    # Calculate assists ranking
    assists_ranking = Player.objects.annotate(total_assists=Sum('assist')).order_by('-total_assists')

    # Calculate goalscorers ranking
    goalscorers_ranking = Player.objects.annotate(total_goals=Sum('goals_scored')).order_by('-total_goals')

    return render(request, 'football_app/tournament_list.html', {
        'tournaments': tournaments,
        'matches_by_tournament': matches_by_tournament,
        'standings': standings,
        'assists_ranking': assists_ranking,
        'goalscorers_ranking': goalscorers_ranking,
    })


def team_detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'football_app/team_detail.html', {'team': team, 'players': players})

