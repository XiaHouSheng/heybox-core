import os
import requests
from Utils.keygen import generate_send_token_origin
from Event.events import EventAt

class ReqBuilder:
    def __init__(self, url):
        self.url = url
        self.data = None
        keys = generate_send_token_origin(url)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "Cookie": os.getenv("COOKIE"),
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
            "host": "api.xiaoheihe.cn",
            "Referer": "https://www.xiaoheihe.cn/",
            "Origin": "https://www.xiaoheihe.cn",
            "Accept": "application/json, text/plain, */*"
        }
        self.params = {
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
            "hkey": keys["hkey"],
            "_time": keys["_time"],
            "nonce": keys["nonce"]
        }

    def body(self, data):
        self.data = data
        return self
    
    def build(self):
        session = requests.Session()
        session.headers = self.headers
        session.params = self.params
        self.session = session
        return self
    
    def get(self):
        self.data = self.session.get(self.url, data=self.data).json()
        return self
    
    def post(self):
        self.data = self.session.post(self.url, data=self.data).json()
        return self

class SendMessageReqBuilder(ReqBuilder):
    def __init__(self, url):
        super().__init__(url)
    
    def send(self, Message):
        self.body(Message.build())
        self.build()
        self.post()

class PollerReqBuilder(ReqBuilder):
    def __init__(self, url):
        super().__init__(url)
        additional_params = {
            "message_type": "16", # 消息类型 16: AT消息
            "offset": "0",
            "limit": "20",
            "no_more": "false"
        }
        self.params.update(additional_params)

    def convertToEvents(self):
        events = []
        for item in self.data["result"]["messages"]:
            event = EventAt()
            event.build(item)
            events.append(event)
        return events