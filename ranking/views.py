from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from ranking.models import Player, Game, Score
from operator import itemgetter

def index(request, year=''):
    years = [str(d.year) for d in Game.objects.dates('play_date', 'year')[::-1]]
    counts = [(y, len(Game.objects.filter(play_date__year=y))) for y in years]
    games = year and get_list_or_404(Game, play_date__year = year) or Game.objects.all()
    scores = year and Score.objects.filter(game__play_date__year=year) or Score.objects.all()
    players = [p for p in scores.values_list('player__name', flat=True).distinct()]
    stats = [(p, scores.filter(player__name=p)) for p in players]

    ranking = []
    for s in stats:
        num_games = len(s[1])
        victories = len([x for x in s[1] if x.score == 10])
        avg_score = "{0:.2f}".format(float(sum([x.score for x in s[1]])) / num_games)
        percent_win = "{0:.2f} %".format(float(victories) / num_games * 100)
        rating = "{0:.0f}".format(float(7.5 + victories) / (50 + num_games) * 10000)
        ranking.append([s[0], rating, percent_win, victories, num_games, avg_score]) 
        
    c = {
            'games': games, 
            'ranking': sorted(ranking, key=itemgetter(1,5), reverse=True), 
            'years': counts,
            'total': len(Game.objects.all()),
            'page': year and year or 'Total',
    }
    return render_to_response('index.html', c, context_instance=RequestContext(request))

