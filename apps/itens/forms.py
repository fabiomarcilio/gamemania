from django import forms

from apps.itens.models import Item, ItemUsuario


class ItemModelForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class ItemModelForm(forms.ModelForm):

    class Meta:
        model = ItemUsuario
        fields = '__all__'
