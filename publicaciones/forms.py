from django import forms
from tagging.models import Tag

class TagForm(forms.Form):
	tag = forms.ModelChoiceField(queryset=Tag.objects.all(), label="Categorias")