from django import forms
from myapp.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__' 