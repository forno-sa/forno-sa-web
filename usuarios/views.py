from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


class Usuario(TemplateView):
    template_name = 'base.html'

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
				return render(request, "index.html")

		return render(request, "login.html")
