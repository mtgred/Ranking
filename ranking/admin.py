from django.contrib import admin
from ranking.models import Game, Player, Score

class ScoreInline(admin.TabularInline):
    model = Score
    extra = 4

class GameAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
    date_hierarchy = 'play_date'

admin.site.register(Game, GameAdmin)
admin.site.register(Player)
