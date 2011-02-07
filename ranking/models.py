from django.db import models
from django.template.defaultfilters import slugify
import datetime

class Player(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/player/%s/" % (self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Player, self).save(*args, **kwargs)

class Game(models.Model):
    play_date = models.DateField(default=datetime.date.today())

    def __unicode__(self):
        return "%s" % (self.play_date)

class Score(models.Model):
    player = models.ForeignKey(Player)
    game = models.ForeignKey(Game)
    score = models.IntegerField()
