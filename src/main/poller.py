from Net.builder import PollerReqBuilder
from Utils.dedup import deduplicator
from Event.dispatcher import event_dispatcher
import logging
import os
import time


poll_interval = int(os.getenv("POLL_INTERVAL"))
poller_url = "https://api.xiaoheihe.cn/bbs/app/user/message"

def startPoller():
    logging.info("开始轮询消息 - 间隔: {}秒".format(poll_interval))
    while True:
        events = PollerReqBuilder(poller_url).build().get().convertToEvents()
        deduplicated_events = deduplicator.process(events)
        event_dispatcher.batch_emit(deduplicated_events)
        logging.info("处理 {} 条事件".format(len(deduplicated_events)))
        time.sleep(poll_interval)

if __name__ == "__main__":
    startPoller()



