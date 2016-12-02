from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Noticias
from publicaciones.models import Publicacion
from eventos.models import Evento
from galerias.models import Galeria


def lista_noticias(request):
    publicaciones = Publicacion.objects.order_by('-id')[:4]
    eventos = Evento.objects.order_by('-id')[:4]
    noticia = Noticias.objects.all()

    paginator = Paginator(noticia, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        objetos = paginator.page(page)
    except  (EmptyPage, InvalidPage):
        objetos = paginator.page(paginator.num_pages)

    return render_to_response('noticias/lista-noticias.html', locals(), 
                                        context_instance=RequestContext(request))

def detalle_noticia(request, slug):
    detalle = get_object_or_404(Noticias, slug=slug)
    
    ultimas = Noticias.objects.all().order_by('-id')[:5]

    return render_to_response('noticias/detalle_noticia.html', {'detalle':detalle, 'ultimas':ultimas},
                                    context_instance=RequestContext(request))

def lista_galerias(request):
    
    eventos = Evento.objects.order_by('-id')[:4]
    noticia = Noticias.objects.order_by('-id')[:4]
    galerias = Galeria.objects.all()

    paginator = Paginator(galerias, 7)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        objetos = paginator.page(page)
    except  (EmptyPage, InvalidPage):
        objetos = paginator.page(paginator.num_pages)

    return render_to_response('galerias/galeria_list.html', locals(), 
                            context_instance=RequestContext(request))