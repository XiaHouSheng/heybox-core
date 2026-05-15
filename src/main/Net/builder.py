import os
import logging
import requests
from requests.exceptions import RequestException, JSONDecodeError
from Utils.keygen import generate_send_token_origin
from Event.events import EventAt
from Utils.dedup import deduplicator

log = logging.getLogger(__name__)

class ReqBuilder:
    def __init__(self, url):
        self.url = url
        self.data = None
        try:
            keys = generate_send_token_origin(url)
        except Exception as e:
            log.error("生成签名失败: {}".format(e))
            raise
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
            "hkey": keys["hkey"],
            "_time": keys["_time"],
            "nonce": keys["nonce"]
        }
    
    def clear_cookie(self):
        self.headers.pop("Cookie", None)

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
        try:
            response = self.session.get(self.url, data=self.data, timeout=30)
            log.debug("GET {} - 状态码: {}".format(self.url, response.status_code))
            self.data = response.json()
        except RequestException as e:
            log.error("网络请求失败 [GET] {}: {}".format(self.url, e))
            raise
        except JSONDecodeError as e:
            log.error("JSON解析失败 [GET] {}: {}".format(self.url, e))
            raise
        except Exception as e:
            log.error("未知错误 [GET] {}: {}".format(self.url, e))
            raise
        return self
    
    def post(self):
        try:
            response = self.session.post(self.url, data=self.data, timeout=30)
            log.debug("POST {} - 状态码: {}".format(self.url, response.status_code))
            self.data = response.json()
        except RequestException as e:
            log.error("网络请求失败 [POST] {}: {}".format(self.url, e))
            raise
        except JSONDecodeError as e:
            log.error("JSON解析失败 [POST] {}: {}".format(self.url, e))
            raise
        except Exception as e:
            log.error("未知错误 [POST] {}: {}".format(self.url, e))
            raise
        return self

class QrCodeReqBuilder(ReqBuilder):
    def __init__(self, url):
        super().__init__(url)
        self.clear_cookie()

class GetQrStatusReqBuilder(ReqBuilder):
    def __init__(self, url):
        super().__init__(url)
        self.params["device_id"] = ""
        self.clear_cookie()
    
    def get(self, qr_code_id: str):
        self.params["qr"] = qr_code_id
        return super().get()

class SendMessageReqBuilder(ReqBuilder):
    def __init__(self, url):
        super().__init__(url)
    
    def send(self, message, message_id):
        try:
            self.body(message.build()).build().post()
            deduplicator.addDeduplicated(str(message_id))
            deduplicator.save()
            log.info("消息发送成功 - MessageID: {}".format(message_id))
        except Exception as e:
            log.error("消息发送失败 - MessageID: {}: {}".format(message_id, e))
            raise

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
        try:
            messages = self.data.get("result", {}).get("messages", [])
            for item in messages:
                event = EventAt()
                event.build(item)
                events.append(event)
        except (KeyError, TypeError) as e:
            log.error("解析消息列表失败: {}".format(e))
        except Exception as e:
            log.error("转换事件时发生未知错误: {}".format(e))
        return events