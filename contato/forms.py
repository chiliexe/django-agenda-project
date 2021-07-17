from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ['name', 'last_name', 'phone', 'email', 'description', 'category']
