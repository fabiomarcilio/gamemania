from attr import attrs
from django import forms

from apps.usuarios.models import Usuario, UFS_SIGLAS


class UsuarioModelForm(forms.ModelForm):

    nome = forms.CharField(required=True, label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(
        attrs={'class': 'form-control mask-cpf'}))
    foto = forms.ImageField(widget=forms.FileInput(attrs={
                            'class': 'form-control',
                            'style': 'display:none',
                            'id': 'foto-input',
                            'required': False,
                            'capture': 'user', 'accept': 'image/*'}))
    data_nascimento = forms.CharField(label='Data de nascimento', widget=forms.DateInput(format='%Y-%m-%d',
                                                                                         attrs={'type': 'date', 'class': 'form-control mask-data'}))
    telefone = forms.CharField(
        label='Telefone', widget=forms.TextInput(attrs={'class': 'form-control mask-telefone'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    redes_sociais = forms.CharField(
        label='Redes Sociais', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(label='CEP', widget=forms.TextInput(
        attrs={'class': 'form-control mask-cep'}))
    logradouro = forms.CharField(
        label='Logradouro', widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(
        label='Bairro', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(
        label='Cidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    uf = forms.ChoiceField(required=True, label='UF', choices=UFS_SIGLAS, widget=forms.Select(
        attrs={'class': 'form-control'}), initial='SP')
    numero = forms.CharField(
        label='Numero', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = [
            'nome', 'cpf', 'foto', 'data_nascimento', 'telefone', 'email',
            'redes_sociais', 'cep', 'logradouro', 'bairro', 'cidade', 'uf', 'numero'
        ]
