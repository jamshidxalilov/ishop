from django.shortcuts import render
from django.views.generic import View
from .forms import RegistrationForm


class RegistrationView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Ro'yxatdan o'tish"
    def get(self, request):
        return render(request, 'client/registration.html', {
            'form': RegistrationForm()
        })
    def post(self, request):
        pass

