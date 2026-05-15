import os 
import dotenv
dotenv.load_dotenv()
from Log.logger import setUpLogger
from Utils.check import checkEnv, checkCookieExpired
from Utils.error import CookieExpiredError
from Event.dispatcher import on
from Event.events import EventAt
from Message.builder import MessageBuilder
from Net.builder import SendMessageReqBuilder
from poller import startPoller

log = setUpLogger()
sender = SendMessageReqBuilder("https://api.xiaoheihe.cn/bbs/app/comment/create")

@on("at")
def handleAt(event: EventAt):
    log.info("收到@消息:{}".format(event.message_id))
    msg = MessageBuilder()
    msg.text("你好").link_id(int(event.link_id)).root_id(int(event.root_id)).reply_id(int(event.root_id))
    sender.send(msg)
    log.info("发送回复:{}".format(msg.build()))
    
if __name__ == "__main__":
    log.info("HeyBoxBot - version 1.0.0")
    try:
        checkEnv()
        checkCookieExpired()
    except FileNotFoundError as e:
        log.error("环境变量检查失败:{}".format(e))
        exit(1)
    except ValueError as e:
        log.error("环境变量检查失败:{}".format(e))
        exit(1)
    except CookieExpiredError as e:
        log.error(e)
        #--> 执行登录流程
    finally:
        #--> 保存日志
        pass

    log.info("当前设备ID:{}".format(os.getenv("DEVICE_ID")))
    log.info("当前账号ID:{}".format(os.getenv("HEYBOX_ID")))
    startPoller()

