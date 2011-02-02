import csv, datetime
from ranking.models import Player, Game, Score

def main(f):
    for row in csv.reader(open(f)):
        d = datetime.date(*[int(x) for x in row[0].split('-')])
        g = Game(play_date=d)
        g.save()
        for col in row[1:]:
            t = col.split()
            p = Player.objects.get_or_create(name=' '.join(t[:-1]))[0]
            Score(player=p, game=g, score=t[-1]).save()
