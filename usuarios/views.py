from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.detail import DetailView
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario, UsuarioManager
from usuarios.forms import CreateUsuarioForm, UpdateUsuarioForm

class Index(TemplateView):
    template_name = 'base.html'

class NBR(TemplateView):
	template_name = "nbr.html"

class Auth(object):
    def login(request):
        if request.method == 'POST':
            matricula = request.POST['matricula']
            senha = request.POST['senha']
            user = authenticate(username=matricula, password=senha)
            if user and user.is_active:
                auth_login(request, user)
                return render(request, 'base.html')
                
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
            request, 'usuarios/login.html',
            {'login_form': AuthenticationForm()})

class CreateUsuarioView(CreateView):
    model = Usuario
    template_name = 'usuarios/create_usuario.html'
    form_class = CreateUsuarioForm
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        self.object = None
        import ipdb; ipdb.set_trace()
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

	
class NBR(TemplateView):
	template_name = "nbr.html"
