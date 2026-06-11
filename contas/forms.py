from django import forms
from django.contrib.auth.models import User


class CadastroForm(forms.Form):
    nome= forms.CharField(max_length=150, label="Nome")
    email= forms.EmailField(label="E-mail")
    senha= forms.CharField(
        widget=forms.PasswordInput,
        label="Senha",
        min_length=6,
        error_messages={"min_length": "Mínimo de 6 caracteres"},
    )

    def clean_email(self):
        email=self.cleaned_data["email"].lower()
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("E-mail já cadastrado")
        return email
    
    def save(self):
        d=self.cleaned_data
        return User.objects.create_user(
            username=d["email"],
            email=d["email"],
            password=d["senha"],
            first_name=d["nome"],
        )
    
class LoginForm(forms.Form):
    email= forms.EmailField(label="E-mail")
    senha= forms.CharField(widget=forms.PasswordInput, label="Senha")