from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm, LoginForm
from financas.models import Categoria
from financas.forms import TransacaoForm

CATEGORIAS_PADRAO = ["Alimentação", "Transporte", "Moradia", "Lazer", "Contas", "Outros"]


def cadastro (request):
    if request.user.is_authenticated:
        #Redireciona direto user logado
        return redirect("home")
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user= form.save()
            Categoria.objects.bulk_create(
                [Categoria(usuario=user, nome=nome) for nome in CATEGORIAS_PADRAO]
            )
            login(request, user)
            return redirect("home")
    else:
        form = CadastroForm()
    return render(request, "contas/cadastro.html", {"form" : form})

@login_required
def home(request):
    form = TransacaoForm(usuario=request.user)
    return render(request, "home.html", {"form": form})


def entrar(request):
    if request.user.is_authenticated:                 
        return redirect("home") #Se tá logado vai pra home direto -> RN-C
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["email"].lower(),
                password=form.cleaned_data["senha"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")
        # Qualquer falha (campo inválido OU credencial errada) -> mensagem genérica (RN-B)
        form.add_error(None, "E-mail ou senha inválidos")
    return render(request, "contas/login.html", {"form": form})


def sair(request):
    logout(request)
    return redirect("login")