from django.db import models
import datetime

class Player(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Game(models.Model):
    play_date = models.DateField(default=datetime.date.today())

    def __unicode__(self):
        return "%s" % (self.play_date)

class Score(models.Model):
    player = models.ForeignKey(Player)
    game = models.ForeignKey(Game)
    score = models.IntegerField()
