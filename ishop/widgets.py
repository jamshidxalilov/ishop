from django.forms.widgets import ClearableFileInput
from django.conf import settings

class ImageRenderWidget(ClearableFileInput):
    template_name = 'widgets/render_image.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context.update({'MEDIA_URL': settings.MEDIA_URL})

        return context