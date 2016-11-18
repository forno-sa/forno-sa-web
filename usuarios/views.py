from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, TemplateView
from .forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


class Usuario(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)

class Auth(object):
	def login(request):
		if request.method == 'POST':
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user and user.is_active:
				auth_login(request, user)
				print ("Tah logado")
				return render(request, "index.html")
		return render(request, "login.html", {"login_form": AuthenticationForm()})

	def logout(request):
		auth_logout(request)
		return render(request, "index.html", {"login_form": AuthenticationForm()})

class NBR(TemplateView):
	template_name = "nbr.html"
