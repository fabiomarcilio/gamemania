from django import forms

from apps.usuarios.models import Usuario


class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
