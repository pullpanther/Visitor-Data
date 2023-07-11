from django.shortcuts import render, redirect
from .functions import *


def visitor(request):
    # https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.META
    meta = request.META

    # https://pypi.org/project/django-user-agents/
    ua = request.user_agent

    ip = get_ip(request)

    geo_data = request.session.get("geolocation")
    if not geo_data:
        geo_data = get_geolocation_data(request)
        request.session["geolocation"] = geo_data

    context = {"meta": meta,
               "ua": ua,
               "ip": ip,
               "geo_data": geo_data,
               }

    return render(request, "visitordata_app/visitor.html", context)
