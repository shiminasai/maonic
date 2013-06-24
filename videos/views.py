from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Video
from noticias.models import Noticias

def lista_videos(request):
	objetos = Video.objects.all()
	ultimas_noticias = Noticias.objects.order_by('-id')[:4]

	return render_to_response('videos/videos_list.html', {'objetos':objetos,
									'ultimas_noticias':ultimas_noticias},
							 context_instance=RequestContext(request))