import requests

# 服务器端的登录URL
LOGIN_URL = "https://clarityvpn.xyz/api/v1/passport/auth/login"
# 服务器端的订阅URL
SUBSCRIBE_URL = "https://clarityvpn.xyz/api/v1/user/getSubscribe"

login_data = {
    "email": "1226619354@qq.com",
    "password": "12345678"
}


def login():
    try:
        response = requests.post(LOGIN_URL, json={"email": login_data['email'], "password": login_data['password']})

        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print("Login successful")
                print("Access Token:", data["data"]["auth_data"])
                return data["data"]["auth_data"]
            else:
                print("Login failed:", data.get("message"))
        else:
            print("An error occurred:", response.status_code, response.text)
    except requests.RequestException as e:
        print("An exception occurred:", str(e))
