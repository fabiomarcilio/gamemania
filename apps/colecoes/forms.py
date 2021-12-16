from django import forms

from apps.colecoes.models import Colecao


class ColecaoModelForm(forms.ModelForm):

    class Meta:
        model = Colecao
        fields = '__all__'
