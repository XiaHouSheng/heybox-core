import logging
class EventDispatcher:
    def __init__(self):
        self.events = {}
    
    def register(self, event_type, handler):
        if event_type not in self.events:
            self.events[event_type] = handler

    def emit(self, event):
        if event.event_type in self.events:
            self.events[event.event_type](event)
            logging.info("{0}事件 MessageID: {1}".format(event.event_type, event.message_id))
    
    def batch_emit(self, events):
        if not events:
            return
        for event in events:
            self.emit(event)

event_dispatcher = EventDispatcher()

def on(event_type):
    def decorator(handler):
        event_dispatcher.register(event_type, handler)
        return handler
    return decorator