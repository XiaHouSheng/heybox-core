# Heybox Core

小黑盒机器人核心 - 基于 Python | The core of Heybox bot based on Python

## 项目简介

本项目是小黑盒（Heybox）社区的 API 封装与自动化工具，提供发送评论、获取消息等核心功能。

## 功能特性

- ✅ 生成请求签名（hkey、nonce、timestamp）
- ✅ 发送评论到小黑盒社区
- ✅ 获取用户消息列表
- ✅ 支持环境变量配置敏感信息

## 项目结构

```
heybox-core/
├── src/
│   ├── encoder_cli/
│   │   └── process_origin.js    # 签名生成核心逻辑
│   └── test/
│       ├── SendMessageTest.py  # 发送消息测试
│       ├── GetSendTokenTest.py # 获取Token测试
│       └── AtGetTest.py        # 获取@消息测试
├── .gitignore
├── LICENSE
└── README.md
```

## 环境要求

- Python 3.8+
- Node.js（用于执行 JavaScript 加密逻辑）

## 安装依赖

```bash
pip install requests python-dotenv PyExecJS
```

## 配置说明

在项目根目录创建 `.env` 文件，配置以下环境变量：

```env
# 用户Cookie（从浏览器获取）
COOKIE=your_cookie_here

# 用户ID
HEYBOX_ID=your_heybox_id

# 设备ID
DEVICE_ID=your_device_id
```

## 使用示例

### 发送评论

```python
from GetSendTokenTest import generate_send_token_origin

# 生成签名
token = generate_send_token_origin()
hkey = token["hkey"]
nonce = token["nonce"]
_time = token["_time"]

# 发送评论逻辑...
```

### 获取消息

```python
from GetSendTokenTest import generate_send_token_origin

# 生成签名并请求消息接口
token = generate_send_token_origin()
# 请求消息逻辑...
```

## API 说明

### 核心方法

| 方法 | 说明 | 返回值 |
|------|------|--------|
| `generate_send_token_origin()` | 生成请求签名 | `{hkey, nonce, _time}` |

### 支持的接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/bbs/app/comment/create` | POST | 发送评论 |
| `/bbs/app/user/message` | GET | 获取消息列表 |

## 注意事项

1. ⚠️ 请妥善保管你的 Cookie，避免泄露
2. ⚠️ 使用本工具请遵守小黑盒社区规定
3. ⚠️ 请勿进行高频请求，避免账号被封禁

## License

MIT License