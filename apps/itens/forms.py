from django import forms

from apps.itens.models import Item
from apps.colecoes.models import Colecao


class ItemModelForm(forms.ModelForm):

    nome = forms.CharField(required=True, label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    descricao = forms.CharField(required=False, label='Descrição',
                                widget=forms.Textarea(attrs={'class': 'form-control capitalizar'}))
    marca = forms.CharField(required=False, label='Marca', widget=forms.TextInput(
        attrs={'class': 'form-control capitalizar'}))
    modelo = forms.CharField(required=False, label='Modelo', widget=forms.TextInput(
        attrs={'class': 'form-control capitalizar'}))
    cor = forms.CharField(required=False, label='Cor', widget=forms.TextInput(
        attrs={'class': 'form-control capitalizar'}))
    data_compra = forms.CharField(label='Data da compra', widget=forms.DateInput(format='%Y-%m-%d',
                                                                                 attrs={'type': 'date', 'class': 'form-control mask-data'}))
    valor_pago = forms.CharField(required=False, label='Valor pago', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    valor_venda = forms.CharField(required=False, label='Valor de venda', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    estado_item = forms.CharField(required=False, label='Estado do item',
                                  widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    disponivel_venda = forms.BooleanField(
        label='Colocar para venda', required=False, initial=False)
    colecao = forms.ModelChoiceField(queryset=Colecao.objects.all(), label='Coleção',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    foto = forms.ImageField(required=False, widget=forms.FileInput(attrs={
                            'class': 'form-control',
                            'style': 'display:none',
                            'id': 'foto-input',
                            'required': False,
                            'capture': 'user', 'accept': 'image/*'}))

    class Meta:
        model = Item
        fields = ['nome', 'descricao', 'marca', 'modelo', 'cor', 'foto']
