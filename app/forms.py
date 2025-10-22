from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:

        model = Aluno

        fields = ['nome', 'matricula']

        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matricula'}),
        }