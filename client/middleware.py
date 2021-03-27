from inspect import getmodule
import django.contrib.admin.sites
from django.http import Http404
import logging

logger = logging.getLogger(__name__)


class RestrictStaffToAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        pass

        if request.path.startwith("/admin/"):
            if request.META.get('REMOTE_ADDR') != '127.0.0.1':
                raise Http404
        response = self.get_response(request)

        return response