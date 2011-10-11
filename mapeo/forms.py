# -*- coding: UTF-8 -*-
from django import forms
from models import *

class ProductoresForm(forms.Form):
    #columna de la izq
    familia = forms.CharField(label='Familia', 
            widget = forms.CheckboxInput)
    asistencia = forms.CharField(label='Asistencia', 
            widget = forms.CheckboxInput)

    #rubros
    cultivos = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroCultivo.objects.all(), label='Rubro Cultivo', 
            required=False)
    animales = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroAnimales.objects.all(), label='Rubro Animales', 
            required=False)
    arboles = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroArboles.objects.all(), label='Rubro Arboles',
            required=False)

    #otros filtros
    semillas = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Semilla.objects.all(), label='Semilla',
            required=False)
    materia_procesada = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=MateriaProcesada.objects.all(), label='Materia Procesada', 
            required=False)
    buenas_practicas = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=BuenasPracticas.objects.all(), label='Buenas prácticas',
            required=False)
    tipo_organizacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=TipoOrganizacion.objects.all(), label='Tipo organización',
            required=False)
    certificacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Certificacion.objects.all(), label='Certificación', 
            required=False)

class AsociacionesForm(forms.Form):
    #columna de la izq
    cooperativa = forms.CharField(label='Cooperativa', 
            widget = forms.CheckboxInput)
    centrales = forms.CharField(label='Centrales', 
            widget = forms.CheckboxInput)

    #rubros
    rubros = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Rubros.objects.all(), label='Rubros', 
            required=False)
    animales = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroAnimales.objects.all(), label='Rubro Animales', 
            required=False)
    arboles = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroArboles.objects.all(), label='Rubro Arboles',
            required=False)

    #otros filtros
    semillas = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Semilla.objects.all(), label='Semilla',
            required=False)
    materia_procesada = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=MateriaProcesada.objects.all(), label='Materia Procesada', 
            required=False)
    buenas_practicas = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=BuenasPracticas.objects.all(), label='Buenas prácticas',
            required=False)
    tipo_organizacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=TipoOrganizacion.objects.all(), label='Tipo organización',
            required=False)
    certificacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Certificacion.objects.all(), label='Certificación', 
            required=False)
