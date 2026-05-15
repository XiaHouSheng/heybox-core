import execjs
import dotenv
dotenv.load_dotenv()

with open("./src/encoder_cli/process_origin.js", "r", encoding="utf-8") as f:
    js_code = f.read()

ctx= execjs.compile(js_code)

def generate_send_token_origin(url = "/bbs/app/comment/create"):
    return ctx.call("getKeys", url)

if __name__ == "__main__":
    print(generate_send_token_origin())

