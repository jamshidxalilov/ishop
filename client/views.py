from django.shortcuts import render

from django.views.generic import TemplateView


class ClientIndex(TemplateView):
    template_name = "client/index.html"

    def get_context_data(self, **kwargs):
        kwargs["text"] = "Hello World!!!"
        return super().get_context_data(**kwargs)

