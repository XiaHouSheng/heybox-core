import qrcode
import dotenv
import logging
import time
from urllib.parse import urlparse
from Net.builder import QrCodeReqBuilder, GetQrStatusReqBuilder


qr_code_get_url = "https://api.xiaoheihe.cn/account/get_qrcode_url/"
qr_code_status_url = "https://api.xiaoheihe.cn/account/qr_state/"
env_path = dotenv.find_dotenv()
qrcode_terminal = qrcode.QRCode(
    version=3,
    box_size=1,
    border=1,
)

def generate_qr_code():
    qr_code_req = QrCodeReqBuilder(qr_code_get_url)
    qr_code_req = qr_code_req.build().post()
    qr_url = qr_code_req.data["result"]["qr_url"]
    qr_code_id = urlparse(qr_url).query.split("=")[1].split("&")[0]
    qrcode_terminal.add_data(qr_url)
    qrcode_terminal.make()
    print("QR Code ID:{}".format(qr_code_id))
    print("QR URL:{}".format(qr_url))
    return qr_code_id

def get_qr_code_status(qr_code_id: str):
    qr_code_req = GetQrStatusReqBuilder(qr_code_status_url)
    qr_code_req = qr_code_req.build().get(qr_code_id) 
    return qr_code_req

def do_login():
    qr_code_id = generate_qr_code()
    for i in range(120):
        qr_code_req = get_qr_code_status(qr_code_id)
        status = qr_code_req.data["result"]["error"]
        print("当前状态:{}".format(status))
        if status == "ok":
            cookie = qr_code_req.session.cookies.get_dict()
            res = ";".join([f"{k}={v}" for k, v in cookie.items()])
            dotenv.set_key(dotenv_path=env_path, key_to_set="COOKIE", value_to_set=res)
            dotenv.load_dotenv(env_path)
            logging.info("登录成功！COOKIE已保存！")
            return
        qrcode_terminal.print_ascii(invert=True)
        time.sleep(5)
    logging.error("登录超时")
    exit(1)


