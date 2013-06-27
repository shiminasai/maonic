from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Publicacion
from tagging.models import Tag, TaggedItem
from .forms import TagForm


def lista_publicaciones(request):
    publicaciones = Publicacion.objects.order_by('-id')
    form = TagForm()

    ultimas_publicaciones = Publicacion.objects.order_by('-id')[:4]
    
    paginator = Paginator(publicaciones, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        objetos = paginator.page(page)
    except  (EmptyPage, InvalidPage):
        objetos = paginator.page(paginator.num_pages)

    return render_to_response('publicaciones/publicaciones.html', locals(), 
                                context_instance=RequestContext(request))

def lista_filtrada(request):
    tag_object = get_object_or_404(Tag, pk=request.POST["tag"])
    publicaciones = TaggedItem.objects.get_by_model(Publicacion(), tag_object)
    #publicaciones = Publicacion.objects.filter(categoria__iregex=r'\b%s\b' % tag).order_by('-id')

    form = TagForm()

    ultimas_publicaciones = Publicacion.objects.order_by('-id')[:4]
    paginator = Paginator(publicaciones, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        objetos = paginator.page(page)
    except  (EmptyPage, InvalidPage):
        objetos = paginator.page(paginator.num_pages)

    return render_to_response('publicaciones/publicaciones.html', locals(), 
                                context_instance=RequestContext(request))