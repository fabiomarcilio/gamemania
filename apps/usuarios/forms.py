from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from dal import autocomplete
from django import forms

from apps.usuarios.models import CustomUsuario, UFS_SIGLAS


class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ['first_name', 'last_name']
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ['first_name', 'last_name']


class UsuarioModelForm(forms.ModelForm):

    first_name = forms.CharField(required=True, label='Nome',
                                 widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    last_name = forms.CharField(required=False, label='Sobrenome',
                                widget=forms.TextInput(attrs={'class': 'form-control capitalizar'}))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(
        attrs={'class': 'form-control mask-cpf'}))
    foto = forms.ImageField(required=False, widget=forms.FileInput(attrs={
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
        model = CustomUsuario
        fields = [
            'first_name', 'last_name', 'cpf', 'foto', 'data_nascimento', 'telefone', 'email',
            'redes_sociais', 'cep', 'logradouro', 'bairro', 'cidade', 'uf', 'numero'
        ]


class UsuarioFiltroIndexForm(forms.Form):
    busca = forms.ChoiceField(
        widget=autocomplete.Select2(
            url='usuario:retornar_usuarios',
            attrs={
                'data-placeholder': 'Todos os registros',
                'data-minimum-input-length': 1,
                'data-theme': 'bootstrap4',
            })
    )
