import requests
from GetSendTokenTest import *
import os

result_test = generate_send_token_origin("/account/get_qrcode_url/")
print(result_test)
hkey = result_test["hkey"]
nonce = result_test["nonce"]
_time = result_test["_time"]

# 你提供的接口 URL
url = "https://api.xiaoheihe.cn/account/get_qrcode_url/"

# 请求参数（全部原样带上）
params = {
    "os_type": "web",
    "app": "web",
    "client_type": "web",
    "version": "999.0.4",
    "web_version": "2.5",
    "x_client_type": "web",
    "x_app": "heybox_website",
    "heybox_id": os.getenv("HEYBOX_ID"),
    "x_os_type": "Windows",
    "device_info": "Chrome",
    "device_id": os.getenv("DEVICE_ID"),
    "hkey": hkey,
    "_time": _time,
    "nonce": nonce,
    "_notip": "true"
}

# 发送 GET 请求
response = requests.get(url, params=params)

# 输出结果
print("状态码:", response.status_code)
print("返回内容:", response.text)