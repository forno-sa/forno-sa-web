from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm

from usuarios.models import Usuario
from usuarios.forms import CreateUsuarioForm, UpdateUsuarioForm

class Index(TemplateView):
    template_name = 'index.html'


class Auth(object):
    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user and user.is_active:
                auth_login(request, user)
                return render(request, 'index.html')
        return render(
            request, 'usuarios/login.html',
            {'login_form': AuthenticationForm()})

    def logout(request):
        auth_logout(request)
        return render(
            request, 'usuarios/index.html',
            {'login_form': AuthenticationForm()})


class CreateUsuarioView(CreateView):
    model = Usuario
    template_name = 'usuarios/create_usuario.html'
    form_class = CreateUsuarioForm


class UpdateUsuarioView(UpdateView):
    model = Usuario
    template_name = 'usuarios/edit_usuario.html'
    form_class = UpdateUsuarioForm


class Icons(TemplateView):
    template_name = 'bootstrap/icons.html'
