from datetime import date
from django import forms
from .models import Transacao, Categoria

class TransacaoForm(forms.ModelForm):
    #Ficha de config
    class Meta:
        model = Transacao #de qual model é
        fields = ["valor", "tipo", "categoria", "data", "descricao"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs) #chama init og do ModelForms
        #usuario=usuario -> Impede leak de categoria
        self.fields["categoria"].queryset = Categoria.objects.filter(usuario=usuario)
        self.fields["categoria"].required = True
        self.fields["categoria"].error_messages = {"required": "Obrigatório"}

        self.fields["descricao"].required = False

        if not self.is_bound: #Veio com dados para POST
            self.fields["data"].initial = date.today()

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        if valor is None or valor <= 0:
            raise forms.ValidationError("Valor deve ser maior que zero")
        return valor

    def save(self, usuario, commit=True):
        obj = super().save(commit=False) #sobrescreve o save do ModelForm
        obj.usuario = usuario
        if not obj.descricao:
            obj.descricao = obj.categoria.nome
        if commit:
            obj.save()
        return obj
