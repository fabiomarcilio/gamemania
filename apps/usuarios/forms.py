from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario

from apps.pessoas.models import Pessoa
from apps.usuarios.models import CustomUsuario


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

    def save(self, commit=True):
        # Instancia um objeto Pessoa para já gravar o id, nome e email já informados no usuario.
        user = super().save(commit=False)
        pessoa, criado = Pessoa.objects.get_or_create(
            email=user.email,
            defaults={
                'id': user.id,
                'nome': user.first_name
            },
        )
        return user
