from django import forms
from .models import *

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre', 'preparación', 'foto')
        permissions = (("can_add_and_delete"),)