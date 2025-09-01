import requests
import base64

def day7():
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
    categories = data.get("data", {}).get("categories", [])

    # Map to activity structure
    activity = [
        {
            "name": cat.get("name"),
            "percent": cat.get("percent"),
            "text": cat.get("text")
        }
        for cat in categories
    ]

    # Print like the Go version
    for a in activity:
        print(f"{a['name']} → {a['text']}\nPercent → {a['percent']}\n")

    return activity

day7()
# if __name__ == "__main__":
#     result = day7()
#     # print("Final JSON:", result)
#     print(result)
