from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class MainIndex(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        kwargs["text"] = "Hello World!!!"
        return super().get_context_data(**kwargs)

