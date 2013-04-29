from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Evento
from noticias.models import Noticias

def lista_evento(request):
	eventos = Evento.objects.order_by('-id')

	ultimas_noticias = Noticias.objects.order_by('-id')[:4]
    
	paginator = Paginator(eventos, 4)

	try:
	    page = int(request.GET.get('page', '1'))
	except ValueError:
	    page = 1

	try:
	    objetos = paginator.page(page)
	except  (EmptyPage, InvalidPage):
	    objetos = paginator.page(paginator.num_pages)

	return render_to_response('eventos/eventos.html', locals(), 
                                context_instance=RequestContext(request))