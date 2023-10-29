from django.conf import settings
import requests


def get_user(pk):
    proxy_base = settings.PROXY_BASE_URL
    proxy_url = f"{proxy_base}/users/{pk}"

    # call flask proxy server
    response = requests.get(proxy_url)
    data = response.json()

    print('data', data)
    if data['error']:
        raise Exception(data['error'])

    return {
        "data": data
    }


def list_users():
    proxy_base = settings.PROXY_BASE_URL
    proxy_url = f"{proxy_base}/users"

    # call flask proxy server
    response = requests.get(proxy_url)
    data = response.json()

    if data['error']:
        raise Exception(data['error'])

    return {
        "data": data
    }

