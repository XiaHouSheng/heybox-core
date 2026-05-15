import json

path = "./src/main/caches/msg/dedup.json"

class Deduplicator:
    def __init__(self):
        self.dedup = set()
        self.load()

    def load(self):
        file = open(path, "r", encoding = "utf-8")
        content = json.load(file)
        self.dedup = set(content["dedup"])

    def save(self):
        with open(path, "w", encoding = "utf-8") as file:
            json.dump({"dedup": list(self.dedup)}, file, ensure_ascii=False, indent=4)

    def isDeduplicated(self, msg_id):
        return str(msg_id) in self.dedup

    def addDeduplicated(self, msg_id):
        self.dedup.add(msg_id)

    def process(self, events: list):
        deduplicated_events = []
        for event in events:
            if self.isDeduplicated(event.message_id):
                continue
            deduplicated_events.append(event)
        return deduplicated_events

deduplicator = Deduplicator()





