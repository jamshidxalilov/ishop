
def current_route_name(request):
    return {
        "crn": "{}:{}".format(request.resolver_match.app_name, request.resolver_match.url_name)
    }