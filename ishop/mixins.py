from django.contrib import messages
from django.shortcuts import redirect


class LogoutRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "Siz tizimga kirgansiz!")
            return redirect('main:index')

        return super().dispatch(request, *args, **kwargs)
