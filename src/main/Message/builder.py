class MessageBuilder:
    def __init__(self):
        self.message = {
            "is_cy": 0,
            "link_id": 0,
            "reply_id": -1,
            "root_id": -1,
            "text": ""
        }

    def link_id(self, link_id):
        self.message["link_id"] = link_id
        return self
    
    def reply_id(self, reply_id):
        self.message["reply_id"] = reply_id
        return self
    
    def root_id(self, root_id):
        self.message["root_id"] = root_id
        return self
    
    def text(self, text):
        self.message["text"] = text
        return self

    def build(self):
        return self.message