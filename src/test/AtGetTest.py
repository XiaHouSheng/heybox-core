# 导入网络请求库（Python最常用的请求工具）
import requests
import os
import dotenv
from GetSendTokenTest import *
dotenv.load_dotenv()

# ===================== 你的核心信息（已自动填入）=====================
# 接口地址
API_URL = "https://api.xiaoheihe.cn/bbs/app/user/message"

# 请求头：包含Cookie（鉴权）+ 浏览器标识（模拟正常访问）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
    "Cookie": os.getenv("COOKIE")
}

result_test = generate_send_token_origin()
print(result_test)
hkey = result_test["hkey"]
nonce = result_test["nonce"]
_time = result_test["_time"]

# 接口请求参数（你之前URL里的所有参数）
PARAMS = {
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
    "message_type": "16",
    "offset": "0",
    "limit": "20",
    "no_more": "false"
}

# ===================== 执行请求 =====================
if __name__ == '__main__':
    try:
        # 发送GET请求
        response = requests.get(API_URL, headers=HEADERS, params=PARAMS)
        # 打印响应状态码（200=成功）
        print(f"请求状态码：{response.status_code}")
        # 打印接口返回的原始数据
        print("\n接口返回数据：")
        print(response.json())
    except Exception as e:
        print(f"请求失败：{e}")