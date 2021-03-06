"""forno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from usuarios.forms import LoginForm
from usuarios.views import (Index, CreateUsuarioView, LoginView, LogoutView,
                            DetailUsuarioView, UpdateUsuarioView, Grafico, NBR)
from tratamento.views import CreateTratamentoView, DetailTratamentoView
from forno.settings import DEBUG


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='inicio'),
    url(r'^grafico/$', Grafico.as_view()),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^nbr/$', NBR.as_view(), name='nbr'),
    url(r'^cadastro-usuario/$',
        CreateUsuarioView.as_view(), name='create-usuario'),
    url(r'^usuario/(?P<pk>\d+)/$',
        DetailUsuarioView.as_view(), name='detail-usuario'),
    url(r'^usuario/(?P<pk>\d+)/edit/$',
        UpdateUsuarioView.as_view(), name='update-usuario'),
    url(r'^tratamento/$', CreateTratamentoView.as_view(),
        name='create-tratamento'),
    url(r'^tratamento/(?P<pk>[0-9]+)/$', DetailTratamentoView.as_view(),
        name='detail-tratamento'),
]

# django debug toolbar
if DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),]
