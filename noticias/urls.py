from django.conf.urls.defaults import *

urlpatterns = patterns('maonic.noticias.views',

    (r'^noticias/$', 'lista_noticias'),
    (r'^detalles/(?P<slug>[-\w]+)/$', 'detalle_noticia'),

)