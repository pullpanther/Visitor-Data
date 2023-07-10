import json
import requests
import time
from .constants import *


def get_ip(request):
    http_header_meta = request.META
    x_forwarded_for = http_header_meta.get('HTTP_X_FORWARDED_FOR')

    # if x_forwarded_for exists, client is connecting through a proxy server
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = http_header_meta.get('REMOTE_ADDR')

    # if in development, localhost ip is 127.0.0.1
    if ip_address == "127.0.0.1":
        time.sleep(1.5)  # avoid 2 api requests at the same time
        data = requests.get(IP_API_URL).content
        time.sleep(1.5)
        geolocation_data = json.loads(data)
        ip_address = geolocation_data.get("ip_address")

    return ip_address


def get_geolocation_data(request):
    ip = get_ip(request)
    data = requests.get(IP_API_URL + "&ip_address=" + ip).content
    geolocation_data = json.loads(data)

    return geolocation_data

