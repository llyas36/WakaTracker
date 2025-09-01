
import requests
from requests.auth import HTTPBasicAuth
# import sys
# import os
# sys.path.append(os.path.abspath("../"))
from handler import http_request

"""

Custom Header...
would like to add HTTP headers to a request,
pass a dict to the headers parameter

"""

baseURL = "https://wakatime.com/api/v1"
api_key = "waka-api"
# def currentUser():
#     # Current logged-in user
#     url = baseURL + "/users/current"
#     #headers = {"Authorization": api_key}
#     response = requests.get(url, auth=HTTPBasicAuth(api_key, ''))
#     return response


def currentUser():
    url = baseURL + "/users/current"
    res = http_request(url, api_key)

    return res

















def meta_data():
    # API metadata
    url = baseURL + "/meta"
    response = requests.get(url, auth=HTTPBasicAuth(api_key, ''))


    return response

def machine_name():
    # Machine names registered under user account
    url = baseURL + "/users/current/machine_names"
    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response

def user_agents():
    # User agents (plugins/editors sending heartbeats)
    url = baseURL + "/users/current/user_agents"
    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response


def account_age():
    if 5 < 2:
        print("five is lessthan 2")
    # all time since account creation...
    url = baseURL + "/users/current/all_time_since_today"

    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response


def daily_summary(start_date, end_date):
    # premium fearture....
    url = baseURL + f"/users/current/summaries?start={start_date}&end={end_date}"

    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response

def Stats():
    # Stats (by language, editor, projects, etc)
    url = baseURL + "/users/current/stats/last_7_days"

    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response

def current_user_project():
    # List user project
    url = baseURL + "/users/current/projects"
    res = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return res

def specific_user_project(projectID):
    # Specific project detail using project id
    url = baseURL + f"/users/current/projects/{projectID}"

    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response


def heart_beats():
    # Heartbeats (raw activity data)

    url = baseURL + "/users/current/heartbeats"

    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response

def durations(date):
    # Durations(aggregated coding sessions lengths)
    url = baseURL + f"/users/current/durations?{date}"
    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response

def goal():
    # List your coding goals
    url = baseURL + "/users/current/goals"

    response = requests.get(url, auth=HTTPBasicAuth(api_key, ""))

    return response

r = Stats()
print(r.encoding)
print(r.text)



# b864c643-d1a3-41f5-9e0f-8ecf20a95c65
