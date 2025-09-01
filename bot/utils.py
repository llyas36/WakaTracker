import requests
import base64
from typing import List, Dict, Any
def weekly_summary(api_key):
    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"


    # Encode Basic Auth
    auth = base64.b64encode(f"{api_key}:".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json"
    }

    # Make the request
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Extract categories
    categories: List[Dict[str, Any]] = data.get("data", {}).get("categories", [])
    languages = data.get("data", {}).get("languages", [])
    projects_raw = data.get("data", {}).get("projects", [])


    # Map to activity structure
    activity: List[Dict[str, Any]] = [
        {
            "name": cat.get("name"),
            "percent": cat.get("percent"),
            "text": cat.get("text")
        }
        for cat in categories
    ]

    languages = [
       {
           "name": lang.get("name"),
           "percent": lang.get("percent"),
           "text": lang.get("text")
       }
       for lang in languages
    ]


    projects = [
        {
            "name": prog.get("name"),
            "percent": prog.get("percent"),
            "text": prog.get("text")
        }
        for prog in projects_raw
     ]





    return activity, languages, projects



def some_stats(api_key):
    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"


    # Encode Basic Auth
    auth = base64.b64encode(f"{api_key}:".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json"
    }

    # Make the request
    response = requests.get(url, headers=headers)

    response.raise_for_status()
    data = response.json()



    machines_raw = data.get("data", {}).get("machines", [])
    editors_raw = data.get("data", {}).get("editors", [])
    os_raw = data.get("data", {}).get("operating_systems", [])

    machines = [
        {
            "name": mach.get("name"),
            "percent": mach.get("percent"),
            "text": mach.get("text")

        }
        for mach in machines_raw
    ]

    editors = [
        {
            "name":editor.get("name"),
            "percent":editor.get("percent"),
            "text":editor.get("text")
        }
        for editor in editors_raw
    ]

    os = [
        {
            "name": o.get("name"),
            "percent":o.get("percent"),
            "text":o.get("text")

        }
        for o in os_raw
    ]


    return machines, editors, os
