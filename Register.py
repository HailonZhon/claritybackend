import requests
# 注册请求数据
register_data = {
    "email": "newuser@example.com",
    "password": "newpassword",
    "invite_code": "optional_invite_code",
    "email_code": "optional_email_code"
}
# 服务器端的注册 URL
REGISTER_URL = "https://clarityvpn.xyz/api/v1/passport/auth/register"
def register(email, password, invite_code=None, email_code=None):
    try:
        # 构建请求数据
        data = {
            "email": email,
            "password": password
        }
        if invite_code:
            data["invite_code"] = invite_code
        if email_code:
            data["email_code"] = email_code

        # 发送 POST 请求
        response = requests.post(REGISTER_URL, json=data)

        # 检查响应状态码
        if response.status_code == 200:
            # 注册成功
            data = response.json()
            print("Registration successful")
            print("Response data:", data)
            return data
        elif response.status_code == 400:
            print("Bad request:", response.json())
        elif response.status_code == 429:
            print("Too many registration attempts, please try again later")
        else:
            print("An error occurred:", response.status_code, response.text)
    except requests.RequestException as e:
        print("An exception occurred:", str(e))

# 调用注册函数
email = "newuser@example.com"
password = "newpassword"
invite_code = "optional_invite_code"  # 如果不需要邀请码，可以去掉这个参数
email_code = "optional_email_code"    # 如果不需要邮箱验证码，可以去掉这个参数
register(email, password, invite_code, email_code)