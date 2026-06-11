from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm, LoginForm


def cadastro (request):
    if request.user.is_authenticated:
        #Redireciona direto user logado
        return redirect("home")
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CadastroForm()
    return render(request, "contas/cadastro.html", {"form" : form})

@login_required
def home(request):
    return render(request, "home.html")


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