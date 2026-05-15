class EventAt:
    def __init__(self):
        self.event_type = "at"
        self.message_id = ""
        self.addition_text = ""
        self.post_title = ""
        self.link_id = ""
        self.root_id = ""
        self.user_id = ""
        self.user_name = ""
        self.time_stamp = 0
    
    def build(self, data):
        self.message_id = data["message_id"]
        self.addition_text = data["comment_a_text"]
        self.post_title = data["link_title"]
        self.link_id = data["linkid"]
        self.root_id = data["root_comment_id"]
        self.user_id = data["userid_a"]
        self.user_name = data["user_a"]["username"]
        self.time_stamp = data["timestamp"]


