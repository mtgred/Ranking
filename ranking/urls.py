from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    (r'^$', 'ranking.views.index'),
    (r'^year/(?P<year>.*)/$', 'ranking.views.index'),
    (r'^player/(?P<slug>.*)/$', 'ranking.views.player'),
)
