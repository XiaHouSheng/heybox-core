import dotenv
import os
import logging
from Net.builder import ReqBuilder
from Utils.error import CookieExpiredError

check_expire = "https://api.xiaoheihe.cn/bbs/app/api/user/permission"

def checkEnv():
    if not os.path.exists("./src/.env"):
        raise FileNotFoundError(".env文件不存在")
    if os.getenv("DEVICE_ID") is None:
        raise ValueError("DEVICE_ID环境变量未设置")
    if os.getenv("HEYBOX_ID") is None:
        raise ValueError("HEYBOX_ID环境变量未设置")
    if os.getenv("COOKIE") is None:
        raise ValueError("COOKIE环境变量未设置")
    logging.info("环境变量检查通过")

def checkCookieExpired():
    result = ReqBuilder(check_expire).build().get().data
    if "status" in result:
        raise CookieExpiredError("COOKIE无效")
    else:
        logging.info("当前设备COOKIE有效")

