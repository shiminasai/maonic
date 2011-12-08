# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from lugar.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import session_required
from django.template import RequestContext
from django.core.exceptions import ViewDoesNotExist, ValidationError
from forms import ProductoresForm, AsociacionesForm
from django.views.generic.simple import direct_to_template

def index(request):
    familias = Familia.objects.all().count()
    cooperativas = Cooperativa.objects.all().count()
    centrales = Centrales.objects.all().count()
    asistencia = AsistenciaTecnica.objects.all().count()
    e_insumos = ComInsumo.objects.all().count()
    e_productos = ComProducto.objects.all().count()
    certificadoras = Certificadora.objects.all().count()
    e_financiera = Financiera.objects.all().count()
    org_publicas = OrgPublica.objects.all().count()

    return direct_to_template(request, 'index.html', locals())

model_dict = {
    'familia': Familia,
    'cooperativa': Cooperativa,
    'centrales': Centrales,
    'asistencia': AsistenciaTecnica,
    'insumo': ComInsumo,
    'producto': ComProducto,
    'certificadora': Certificadora,
    'financiera': Financiera,
    'orgpublica': OrgPublica,
    }

@session_required
def obtener_lista_paginada(request, modelo):
    '''Vista ajax para obtener lista de elementos en
    la vista luego del filtrado, modelo es una cadena
    definida dentro del diccionario model_dict en las
    primeras lineas de este archivo
    '''
    if request.is_ajax():
        params = _get_params(request.session)
        lista_objetos = _get_model(modelo, request.session).objects.filter(**params).distinct()
        paginator = Paginator(lista_objetos, 25)

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            objetos = paginator.page(page)
        except  (EmptyPage, InvalidPage):
            objetos = paginator.page(paginator.num_pages)

        #se le agrega el tipo de modelo para construir la url
        lista_objetos = [dict(objeto, modelo = modelo) for objeto
                in objetos.object_list.values('id', 'nombre','municipio__nombre','telefono','celular','email')]
        resultados = dict(enlaces = lista_objetos,
                          sig = objetos.next_page_number(),
                          ant = objetos.previous_page_number())
        return HttpResponse(simplejson.dumps(resultados), mimetype="application/json")

def obtener_lista_territorio(request, modelo):
    '''Vista ajax para obtener lista de elementos en
    la vista luego del filtrado, modelo es una cadena
    definida dentro del diccionario model_dict en las
    primeras lineas de este archivo
    '''
    if request.is_ajax():
        if request.session['departamento'] == '1':
            lista_objetos = _get_model(modelo).objects.all()
        else:
            lista_objetos = _get_model(modelo).objects.filter(
                municipio__departamento__id = request.session['departamento'])
        paginator = Paginator(lista_objetos, 25)

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            objetos = paginator.page(page)
        except  (EmptyPage, InvalidPage):
            objetos = paginator.page(paginator.num_pages)

        #se le agrega el tipo de modelo para construir la url
        lista_objetos = [dict(objeto, modelo = modelo) for objeto
                in objetos.object_list.values('id', 'nombre','municipio__nombre','telefono','celular','email')]
        resultados = dict(enlaces = lista_objetos,
                          sig = objetos.next_page_number(),
                          ant = objetos.previous_page_number())
        return HttpResponse(simplejson.dumps(resultados), mimetype="application/json")

@session_required
def obtener_lista(request, modelo):
    if request.is_ajax():
        lista = []
        params = _get_params(request.session)
        for objeto in _get_model(modelo).objects.filter(** params).distinct():
            if objeto.lat and objeto.lon:
                dicc = dict(nombre=objeto.nombre, id=objeto.id,
                            lon=foat(objeto.lon) , lat=float(objeto.lat),
                            modelo= modelo)
            else:
                dicc = dict(nombre=objeto.nombre, id=objeto.id,
                            lon=float(objeto.municipio.longitud) ,
                            lat=float(objeto.municipio.latitud),
                            modelo= modelo)
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

def formulario(request):
    if request.method == 'POST':
        form = ProductoresForm(request.POST)
        if form.is_valid():
            lista_modelos = []
            for key in model_dict.keys():
                if key in form.cleaned_data and form.cleaned_data[key] == 'on':
                    lista_modelos.append(key)

            request.session['lista_modelos'] = lista_modelos           

            for coso in ('semillas', 'materia_procesada', 'buenas_practicas',
                    'arboles', 'cultivos', 'animales',
                    'tipo_organizacion', 'certificacion', 'area_trabajo'):
                if coso in form.cleaned_data:
                    request.session[coso] = form.cleaned_data[coso]
                                
            request.session['activo'] = True
            return HttpResponseRedirect('/mapeo/mapa')            
    else:
        form = ProductoresForm()

    return render_to_response('mapeo/formulario.html',
            {'form': form},
            context_instance=RequestContext(request))

def formulario_asociaciones(request):
    if request.method == 'POST':
        form = AsociacionesForm(request.POST)
        if form.is_valid():
            lista_modelos = []
            for key in model_dict.keys():
                if key in form.cleaned_data and form.cleaned_data[key] == 'on':
                    lista_modelos.append(key)

            request.session['lista_modelos'] = lista_modelos

            for coso in ('semillas', 'materia_procesada', 'buenas_practicas',
                    'arboles', 'cultivos', 'animales', 'rubros',
                    'tipo_organizacion', 'certificacion', 'area_trabajo'):
                if coso in form.cleaned_data:
                    request.session[coso] = form.cleaned_data[coso]
            request.session['activo'] = True

            return HttpResponseRedirect('/mapeo/mapa')
    else:
        form = AsociacionesForm()

    return render_to_response('mapeo/formulario_asociaciones.html',
            {'form': form},
            context_instance=RequestContext(request))

def _get_params(session):
    '''funcion interna para devolver parametros
    del formulario de busqueda'''
    keys = ('semillas', 'materia_procesada', 'buenas_practicas',
            'arboles', 'cultivos', 'animales', 'rubros',
            'tipo_org', 'certificacion', 'area_trabajo')
    params = {}
    for key in keys:
        param_key = key + '__in'
        try:
            if session[key] != []:
                params[param_key] = session[key]
        except:
            pass                             
        
    return params

def _get_model(model, session=None):
    if model in model_dict:
        if session:
            if model in session['lista_modelos']:
                return model_dict[model]
            else:
                raise ValidationError('Modelo no esta en sesion')
        else:
            return model_dict[model]

    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))

@session_required
def mapa(request):
    return render_to_response('mapeo/mapa.html',
            {'lista_modelos': request.session['lista_modelos']},
            context_instance=RequestContext(request))

def ficha(request, modelo, id):
    '''Retorna ficha, plantillas cargadas dinamicamente'''
    objeto = get_object_or_404(_get_model(modelo), id=id)
    template_name = 'mapeo/ficha_%s.html' % modelo
    return render_to_response(template_name, {'objeto': objeto},
            context_instance=RequestContext(request))

def galeria(request, modelo, id):
    '''Retorna vista a galeria de fotos'''
    objeto = get_object_or_404(_get_model(modelo), id=id)
    return render_to_response('mapeo/galeria.html', {'objeto': objeto},
            context_instance=RequestContext(request))

@session_required
def lista(request):
    lista_modelos = request.session['lista_modelos']
    params = _get_params(request.session)
    dicc = {'lista_modelos': lista_modelos,
        'familia': 0,
        'cooperativa': 0,
        'centrales': 0,
        'asistencia': 0,
        'insumo': 0,
        'producto': 0,
        'certificadora': 0,
        'financiera': 0,
        'orgpublica': 0,
    }
    for modelo in lista_modelos:
        dicc[modelo] = _get_model(modelo).objects.filter(**params).distinct().count()

    return render_to_response('mapeo/lista.html',
            dicc,
            context_instance=RequestContext(request))

def territorio(request, id=None):
    """
    Mapeo por Territorio, muestra lista de actores ubicados en un departamento.
    """
    if id:
        request.session['departamento'] = id
        lista_modelos = [model for model in model_dict]
        if id == '1':
            cantidad_actores = Familia.objects.all().count() + \
                                Cooperativa.objects.all().count() + \
                                Centrales.objects.all().count() + \
                                AsistenciaTecnica.objects.all().count() + \
                                ComInsumo.objects.all().count() + \
                                ComProducto.objects.all().count() + \
                                Certificadora.objects.all().count() + \
                                Financiera.objects.all().count() + \
                                OrgPublica.objects.all().count() 
            dpto="Todo el pais"
        else:
            cantidad_actores = Familia.objects.filter(municipio__departamento__id = id).count() + \
                                Cooperativa.objects.filter(municipio__departamento__id = id).count() + \
                                Centrales.objects.filter(municipio__departamento__id = id).count() + \
                                AsistenciaTecnica.objects.filter(municipio__departamento__id = id).count() + \
                                ComInsumo.objects.filter(municipio__departamento__id = id).count() + \
                                ComProducto.objects.filter(municipio__departamento__id = id).count() + \
                                Certificadora.objects.filter(municipio__departamento__id = id).count() + \
                                Financiera.objects.filter(municipio__departamento__id = id).count() + \
                                OrgPublica.objects.filter(municipio__departamento__id = id).count() 
            dpto = Departamento.objects.get(pk=id)
        dicc = {'lista_modelos': lista_modelos,
            'familia': 0,
            'cooperativa': 0,
            'centrales': 0,
            'asistencia': 0,
            'insumo': 0,
            'producto': 0,
            'certificadora': 0,
            'financiera': 0,
            'orgpublica': 0,
            'cantidad_actores':cantidad_actores,
            'dpto':dpto,
            'id':id,
        }
        for modelo in lista_modelos:
            if id == '1':
                dicc[modelo] = _get_model(modelo).objects.all().distinct().count()
            else:
                dicc[modelo] = _get_model(modelo).objects.filter(
                    municipio__departamento__id=id).distinct().count()

        return render_to_response('mapeo/lista_territorio.html',
            dicc,
            context_instance=RequestContext(request)
        )
    else:
        return render_to_response('mapeo/territorio.html',
            context_instance=RequestContext(request)
        )
