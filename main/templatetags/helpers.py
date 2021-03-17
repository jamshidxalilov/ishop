from django import template


register = template.Library()

@register.filter
def is_current(input):
    request.resolver_match.app_name == 'main' and request.resolver_match.url_name == 'index'