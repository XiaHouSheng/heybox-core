import execjs
from urllib.parse import urlparse

with open("./src/encoder_cli/process_origin.js", "r", encoding="utf-8") as f:
    js_code = f.read()

ctx= execjs.compile(js_code)

def clean_path(full_url):
    parsed = urlparse(full_url)
    path = parsed.path
    parts = [p for p in path.split("/") if p]
    return f"/{'/'.join(parts)}/"

def generate_send_token_origin(url = "/bbs/app/comment/create"):
    url_process = clean_path(url)
    return ctx.call("getKeys", url_process)

if __name__ == "__main__":
    print(generate_send_token_origin("https://api.xiaoheihe.cn/bbs/app/api/user/permission"))

