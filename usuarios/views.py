from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario, UsuarioManager
from usuarios.forms import CreateUsuarioForm, UpdateUsuarioForm

class Index(TemplateView):
    template_name = 'base.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)

class NBR(TemplateView):
	template_name = "nbr.html"

class Auth(object):
    def login(request):
        if request.method == 'POST':
            matricula = request.POST['matricula']
            senha = request.POST['senha']
            user = authenticate(matricula=matricula, senha=senha)
            if user and user.is_active:
                auth_login(request, user)
                return render(request, 'usuarios/index.html')
                
            if user is not None:
                if user.is_active:
                    print ("Você forneceu um username e senha corretos!")
                else:
                    print ("Sua conta foi desabilitada!")
            else:
                print ("Seu username e senha estavam incorretos.")

            
        return render(
            request, 'usuarios/login.html',
            {'login_form': AuthenticationForm()})

    def logout(request):
        auth_logout(request)
        return render(
            request, 'usuarios/index.html',
            {'login_form': AuthenticationForm()})

    def register(request):
        if request.method == 'POST':
            form = CreateUsuarioForm(data=request.POST)

            if form.is_valid():
                Usuario.objects.create_user(form)
                return render(
                	request, 'usuarios/index.html', 
                	{'login_form': AuthenticationForm()})
            else:
                print(form.errors)
        else:
            form = CreateUsuarioForm()

        return render(
        	request, 'usuarios/create_usuario.html', 
        	{'form': form, 'login_form': AuthenticationForm()})


class CreateUsuarioView(CreateView):
    model = Usuario
    template_name = 'usuarios/create_usuario.html'
    form_class = CreateUsuarioForm
    success_url = reverse_lazy('login')


class UpdateUsuarioView(UpdateView):
    model = Usuario
    template_name = 'usuarios/edit_usuario.html'
    form_class = UpdateUsuarioForm
