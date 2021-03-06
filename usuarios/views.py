from django.shortcuts import render, render_to_response
from django.views.generic import (CreateView, ListView, UpdateView,
                                  TemplateView, FormView, View,)
from django.views.generic.edit import ModelFormMixin
from django.views.generic.detail import DetailView
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from usuarios.models import Usuario
from usuarios.forms import CreateUsuarioForm, UpdateUsuarioForm, LoginForm


class Index(TemplateView):
    template_name = 'base.html'


class NBR(TemplateView):
    template_name = 'pages/nbr.html'


class LoginView(FormView):
    template_name = 'usuarios/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponseRedirect(reverse('inicio'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(reverse('inicio'))


class CreateUsuarioView(CreateView):
    model = Usuario
    template_name = 'usuarios/create_usuario.html'
    form_class = CreateUsuarioForm
    success_url = 'inicio'

    def form_valid(self, form):
        user = User.objects.create_superuser(
            first_name=form.cleaned_data['nome'],
            last_name=form.cleaned_data['sobrenome'],
            username=form.cleaned_data['matricula'],
            password=form.cleaned_data['senha'],
            email=form.cleaned_data['email'],)
        user.save()
        usuario = Usuario(
            user=user, nome=form.cleaned_data['nome'],
            sobrenome=form.cleaned_data['sobrenome'],
            matricula=form.cleaned_data['matricula'],
            email=form.cleaned_data['email'],)
        usuario.save()

        self.object = usuario
        return super(ModelFormMixin, self).form_valid(form)


class DetailUsuarioView(DetailView):
    model = Usuario
    template_name = 'usuarios/detail_usuario.html'


class UpdateUsuarioView(UpdateView):
    model = Usuario
    template_name = 'usuarios/update_usuario.html'
    form_class = UpdateUsuarioForm

    def form_valid(self, form):
        user = User.objects.get(username=form.cleaned_data['matricula'])
        usuario = Usuario.objects.get(user=user)

        user.first_name = form.cleaned_data['nome']
        user.last_name = form.cleaned_data['sobrenome']
        user.email = form.cleaned_data['email']
        user.save()

        usuario.nome = form.cleaned_data['nome']
        usuario.sobrenome = form.cleaned_data['sobrenome']
        usuario.matricula = form.cleaned_data['matricula']
        usuario.email = form.cleaned_data['email']
        usuario.save()

        self.object = usuario
        return super(ModelFormMixin, self).form_valid(form)

    def get_success_url(self):
        pk = self.object.id
        url_reverse = reverse('detail-usuario', kwargs={'pk': pk})
        return url_reverse


class Grafico(TemplateView):
	template_name = 'grafico.html'
