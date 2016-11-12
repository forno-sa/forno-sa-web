from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, TemplateView


class Usuario(TemplateView):
    template_name = 'base.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)
	
class NBR(TemplateView):
	template_name = "nbr.html"