import requests

from Xboard.Login import login

# 服务器端的订阅URL
SUBSCRIBE_URL = "https://clarityvpn.xyz/api/v1/user/getSubscribe"


def get_subscribe_link(access_token):
    headers = {
        "Authorization": f"{access_token}"
    }
    try:
        response = requests.get(SUBSCRIBE_URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print("Subscription link retrieved successfully")
                print("Subscribe URL:", data["data"]["subscribe_url"])
            else:
                print("Failed to retrieve subscription link:", data.get("message"))
        else:
            print("Failed to retrieve subscription link:", response.status_code, response.text)
    except requests.RequestException as e:
        print("An exception occurred:", str(e))


token = login()

if token:
    get_subscribe_link(token)
