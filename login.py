import requests
# 模拟的服务器端登录URL
LOGIN_URL = "https://clarityvpn.xyz/api/v1/passport/auth/login"
# 定义登录请求的数据
login_data = {
    "email": "1226619354@qq.com",
    "password": "12345678"
}


def login(email, password):
    try:
        # 发送POST请求
        response = requests.post(LOGIN_URL, json={"email": email, "password": password})

        # 检查响应状态码
        if response.status_code == 200:
            # 登录成功，返回Token
            data = response.json()
            print("Login successful")
            # print("Access Token:", data["access_token"])
            # return data["access_token"]
            print(data)
            return data
        elif response.status_code == 400:
            print("Incorrect email or password")
        elif response.status_code == 429:
            print("Too many login attempts, please try again later")
        else:
            print("An error occurred:", response.status_code, response.text)
    except requests.RequestException as e:
        print("An exception occurred:", str(e))


# 调用登录函数
email = "1226619354@qq.com"
password = "12345678"
token = login(email, password)