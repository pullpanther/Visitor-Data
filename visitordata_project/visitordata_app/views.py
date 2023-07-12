from django.shortcuts import render, redirect
from .functions import *


def visitor(request):
    # https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.META
    meta = request.META

    # https://pypi.org/project/django-user-agents/
    ua = request.user_agent

    ip = get_ip(request)

    geo_data = request.session.get("geolocation")
    is_from_session = True
    if not geo_data:
        geo_data = get_geolocation_data(request)
        is_from_session = False
        request.session["geolocation"] = geo_data

    context = {"meta": meta,
               "ua": ua,
               "ip": ip,
               "geo_data": geo_data,
               "is_from_session": is_from_session,
               }

    return render(request, "visitordata_app/visitor.html", context)


def delete_session_item(request):
    # url parameters ?item=abc&next=xyz
    item = request.GET.get("item", "")
    next_page = request.GET.get("next", "")

    try:
        del request.session[item]
    # if url item parameter does not exist in session, delete complete session
    except KeyError:
        request.session.flush()

    if next_page:
        return redirect(next_page)

    return redirect("homepage")
