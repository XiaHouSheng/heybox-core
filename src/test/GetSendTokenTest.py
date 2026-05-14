import execjs
with open("./src/encoder_cli/process_origin.js", "r", encoding="utf-8") as f:
    js_code = f.read()

ctx= execjs.compile(js_code)

def generate_send_token_origin():
    return ctx.call("getKeys", "/bbs/app/comment/create")

if __name__ == "__main__":
    print(generate_send_token_origin())

