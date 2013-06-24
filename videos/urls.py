from django.conf.urls.defaults import *

urlpatterns = patterns('maonic.videos.views',

    (r'^lista/$', 'lista_videos'),

)