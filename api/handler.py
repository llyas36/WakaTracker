import requests
from requests.models import HTTPBasicAuth


def http_request(url, api_key ):

    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response



# https://wakatime.com/api/v1//users/current
