import logging

log = logging.getLogger(__name__)

class EventDispatcher:
    def __init__(self):
        self.events = {}
    
    def register(self, event_type, handler):
        if event_type not in self.events:
            self.events[event_type] = handler
            log.debug("注册事件处理器: {}".format(event_type))

    def emit(self, event):
        if event.event_type in self.events:
            try:
                self.events[event.event_type](event)
                log.info("{}事件 MessageID: {}".format(event.event_type, event.message_id))
            except Exception as e:
                log.error("处理{}事件时发生错误 - MessageID: {}: {}".format(
                    event.event_type, event.message_id, e))
    
    def batch_emit(self, events):
        if not events:
            return
        success_count = 0
        error_count = 0
        for event in events:
            try:
                self.emit(event)
                success_count += 1
            except Exception as e:
                log.error("批量处理事件时发生未捕获异常: {}".format(e))
                error_count += 1
        
        if error_count > 0:
            log.warning("批量事件处理完成 - 成功: {}, 失败: {}".format(success_count, error_count))

event_dispatcher = EventDispatcher()

def on(event_type):
    def decorator(handler):
        event_dispatcher.register(event_type, handler)
        log.info("装饰器注册事件: {} -> {}".format(event_type, handler.__name__))
        return handler
    return decorator