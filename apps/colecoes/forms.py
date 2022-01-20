from django import forms

from apps.colecoes.models import Colecao
from apps.usuarios.models import Usuario


class ColecaoModelForm(forms.ModelForm):

    usuario = forms.ModelChoiceField(
        required=False,
        queryset=Usuario.objects.all(), widget=forms.Select())
    nome = forms.CharField(required=True, label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    descricao = forms.CharField(required=False, label='Descrição',
                                widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    data_inicio = forms.CharField(label='Data de inicio', widget=forms.DateInput(format='%Y-%m-%d',
                                                                                 attrs={'type': 'date', 'class': 'form-control mask-data'}))
    valor_estimado = forms.CharField(required=False, label='Valor estimado', widget=forms.TextInput(
        attrs={'class': 'form-control capitalizar'}))
    foto = forms.ImageField()

    class Meta:
        model = Colecao
        fields = ['usuario', 'nome', 'descricao',
                  'data_inicio', 'valor_estimado', 'foto']
