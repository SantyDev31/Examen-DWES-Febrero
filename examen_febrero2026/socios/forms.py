from django import forms
from .models import Disco

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['titulo', 'formato', 'año', 'num_pistas']

    def save(self, commit=True):
        # Guardar el autor
        disco = super().save(commit=False)
        if commit:
            disco.save()
        return disco