from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from ranking.models import Player, Game, Score

def index(request, year=''):
    games = year and get_list_or_404(Game, play_date__year = year) or Game.objects.all()
    c = {
            'games': games, 
            'years': [str(d.year) for d in Game.objects.dates('play_date', 'year')],
            'page': year and year or 'Total',
    }
    return render_to_response('index.html', c, context_instance=RequestContext(request))

