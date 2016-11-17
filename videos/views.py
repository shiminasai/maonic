from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage


from .models import Video
from noticias.models import Noticias
from eventos.models import Evento

def lista_videos(request):
    videos = Video.objects.order_by('-id')
    ultimas_noticias = Noticias.objects.order_by('-id')[:4]
    eventos = Evento.objects.order_by('-id')[:4]

    paginator = Paginator(videos, 3)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        objetos = paginator.page(page)
    except  (EmptyPage, InvalidPage):
        objetos = paginator.page(paginator.num_pages)
            

    return render_to_response('videos/videos_list.html', locals(),
                             context_instance=RequestContext(request))