from django.conf.urls.defaults import *

urlpatterns = patterns('maonic.publicaciones.views',

    (r'^lista/$', 'lista_publicaciones'),
    (r'^filtrar/$', 'lista_filtrada'),

)