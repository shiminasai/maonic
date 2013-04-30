from django.conf.urls.defaults import *

urlpatterns = patterns('maonic.eventos.views',

    (r'^lista/$', 'lista_evento'),
    
)