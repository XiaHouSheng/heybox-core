import requests
import time  # 用于生成当前时间戳
import os
import dotenv
from GetSendTokenTest import *

dotenv.load_dotenv()

result_test = generate_send_token_origin("/bbs/app/comment/create")
print(result_test)
hkey = result_test["hkey"]
nonce = result_test["nonce"]
_time = result_test["_time"]


# ===================== 配置区 =====================
API_URL = "https://api.xiaoheihe.cn/bbs/app/comment/create"

# 请求头（你的Cookie）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
    "Cookie": os.getenv("COOKIE"),
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "host": "api.xiaoheihe.cn",
    "Referer": "https://www.xiaoheihe.cn/",
    "Origin": "https://www.xiaoheihe.cn",
    "Accept": "application/json, text/plain, */*"
}

# URL参数
PARAMS = {
    "os_type": "web",
    "app": "heybox",
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
    "nonce": nonce
}

# 表单数据：link_id 已替换为【当前时间戳】
FORM_DATA = {
    "is_cy": 0,
    "link_id": 179392738,  #这个是目标评论的link_id
    "reply_id": -1,
    "root_id": -1,
    "text": "感谢分享lz12"
}

# ===================== 执行请求 =====================
if __name__ == '__main__':
    try:
        res = requests.post(API_URL, headers=HEADERS, params=PARAMS, data=FORM_DATA)
        print(f"请求状态码：{res.status_code}")
        print("接口响应：", res.json())
    except Exception as e:
        print("请求失败：", e)