from Net.builder import PollerReqBuilder
from Utils.dedup import deduplicator
from Event.dispatcher import event_dispatcher
import logging
import os
import time

log = logging.getLogger(__name__)

poll_interval = int(os.getenv("POLL_INTERVAL", "10"))
poller_url = "https://api.xiaoheihe.cn/bbs/app/user/message"

def startPoller():
    log.info("开始轮询消息 - 间隔: {}秒".format(poll_interval))
    while True:
        try:
            events = PollerReqBuilder(poller_url).build().get().convertToEvents()
            deduplicated_events = deduplicator.process(events)
            event_dispatcher.batch_emit(deduplicated_events)
            log.info("处理 {} 条事件".format(len(deduplicated_events)))
        except Exception as e:
            log.error("轮询过程中发生错误: {}".format(e))
        
        try:
            time.sleep(poll_interval)
        except KeyboardInterrupt:
            log.info("收到中断信号，停止轮询")
            break
        except Exception as e:
            log.error("休眠时发生错误: {}".format(e))

if __name__ == "__main__":
    startPoller()



