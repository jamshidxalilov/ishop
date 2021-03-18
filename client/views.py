from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from ishop.mixins import LogoutRequiredMixin

class RegistrationView(LogoutRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Ro'yxatdan o'tish"


    def get(self, request):
        return render(request, 'client/registration.html', {
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, "{} ro'yxatdan muvaffaqiyatli o'tdingiz.".format(user.get_short_name()))
            return redirect('main:index')

        return render(request, 'client/registration.html', {
            'form': form
        })

class LoginView(LogoutRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Tizimga kirish"


    def get(self, request):
        return render(request, 'client/login.html', {
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, "{} xush kelibsiz!!!".format(user.get_short_name()))

                return redirect('main:index')
            form.add_error('password', "Login va/yoki parol noto'g'ri.")


        return render(request, 'client/login.html', {
            'form': form
        })


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "Kelib turing!!!")

        return redirect('main:index')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        pass
