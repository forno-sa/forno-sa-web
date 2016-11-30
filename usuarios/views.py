from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.detail import DetailView
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse

from django.contrib.auth.models import User
from usuarios.models import Usuario
from usuarios.forms import CreateUsuarioForm, UpdateUsuarioForm

class Index(TemplateView):
    template_name = 'base.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)

class NBR(TemplateView):
	template_name = "pages/nbr.html"

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

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user = User(username=form.cleaned_data['matricula'],
                    password=form.cleaned_data['senha'],
                    email=form.cleaned_data['email'],)
        user.save()
        usuario = Usuario(user=user, nome=form.cleaned_data['nome'],
                          sobrenome=form.cleaned_data['sobrenome'],
                          matricula=form.cleaned_data['matricula'],)
        usuario.save()

        self.object = usuario
        return super(ModelFormMixin, self).form_valid(form)

    def get_success_url(self):
        pk = self.object.id
        url_reverse = reverse('detail-usuario', kwargs={'pk': pk})
        return url_reverse


class DetailUsuarioView(DetailView):
    model = Usuario
    template_name = 'usuarios/detail_usuario.html'

    def get_context_data(self, **kwargs):
        context = super(DetailUsuarioView, self).get_context_data(**kwargs)
        return context


class UpdateUsuarioView(UpdateView):
    model = Usuario
    template_name = 'usuarios/update_usuario.html'
    form_class = UpdateUsuarioForm


class Grafico(TemplateView):
	template_name = 'grafico.html'
