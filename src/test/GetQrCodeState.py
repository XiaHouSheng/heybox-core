import requests
import os
from GetSendTokenTest import *
import time
result_test = generate_send_token_origin("/account/qr_state/")
print(result_test)
hkey = result_test["hkey"]
nonce = result_test["nonce"]
_time = result_test["_time"]

url = "https://api.xiaoheihe.cn/account/qr_state/"

params = {
    "os_type": "web",
    "app": "web",
    "client_type": "web",
    "version": "999.0.4",
    "web_version": "2.5",
    "x_client_type": "web",
    "x_app": "heybox_website",
    "heybox_id": "",
    "x_os_type": "Windows",
    "device_info": "Chrome",
    "device_id": os.getenv("DEVICE_ID"),
    "hkey": hkey,
    "_time": _time,
    "nonce": nonce, 
    "qr": "bb00e846-5027-11f1-9a50-be8d298d9e02"
}
while True:
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        result_json = resp.json()
        if result_json["result"]["error"] == "ok":
            print("COOKIE:", resp.cookies.get_dict())
    print("状态码:", resp.status_code)
    print("返回内容:", resp.text)
    time.sleep(1)

#key = error | value = wait ready cancel ok