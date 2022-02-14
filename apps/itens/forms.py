from django import forms

from apps.itens.models import Item


class ItemModelForm(forms.ModelForm):

    nome = forms.CharField(required=True, label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    descricao = forms.CharField(required=False, label='Descrição',
                                widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    marca = forms.CharField(required=False, label='Marca', widget=forms.TextInput(
        attrs={'class': 'form-control capitalizar'}))
    modelo = forms.CharField(required=False, label='Modelo', widget=forms.TextInput(
        attrs={'class': 'form-control capitalizar'}))
    cor = forms.CharField(required=False, label='Cor', widget=forms.TextInput(
        attrs={'class': 'form-control capitalizar'}))
    foto = forms.ImageField(widget=forms.FileInput(attrs={
                            'class': 'form-control',
                            'style': 'display:none',
                            'id': 'foto-input',
                            'required': False,
                            'capture': 'user', 'accept': 'image/*'}))

    class Meta:
        model = Item
        fields = ['nome', 'descricao', 'marca', 'modelo', 'cor', 'foto']
