# Heybox Core

小黑盒机器人核心 - 基于 Python | Heybox Bot Core based on Python

## 项目简介

Heybox Core 是一个功能完整的小黑盒（Heybox）社区机器人框架，支持消息监听、事件处理、自动回复等核心功能。

## 功能特性

- ✅ 请求签名生成（hkey、nonce、timestamp）
- ✅ 消息轮询与事件分发
- ✅ @消息自动回复
- ✅ 消息去重机制
- ✅ Cookie 有效期检测
- ✅ 完整的日志系统

## 项目结构

```
heybox-core/
├── src/
│   ├── main/                    # 主程序目录
│   │   ├── Event/              # 事件系统
│   │   │   ├── dispatcher.py   # 事件分发器
│   │   │   └── events.py       # 事件定义
│   │   ├── Log/                # 日志模块
│   │   │   ├── __init__.py
│   │   │   └── logger.py       # 日志配置
│   │   ├── Message/            # 消息构建
│   │   │   ├── __init__.py
│   │   │   └── builder.py      # 消息构建器
│   │   ├── Net/                # 网络请求
│   │   │   ├── __init__.py
│   │   │   └── builder.py      # 请求构建器
│   │   ├── Utils/              # 工具类
│   │   │   ├── __init__.py
│   │   │   ├── check.py        # 环境检查
│   │   │   ├── dedup.py        # 去重处理
│   │   │   ├── error.py        # 错误定义
│   │   │   └── keygen.py       # 签名生成
│   │   ├── caches/             # 缓存目录
│   │   │   └── msg/            # 消息缓存
│   │   ├── bot.py              # 机器人主入口
│   │   └── poller.py           # 消息轮询器
│   ├── encoder_cli/            # JavaScript加密逻辑
│   │   └── process_origin.js   # 签名生成核心
│   ├── note/                   # 备注文件
│   └── test/                   # 测试脚本
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

在项目根目录创建 `.env` 文件：

```env
# 用户Cookie（从浏览器获取）
COOKIE=your_cookie_here

# 用户ID
HEYBOX_ID=your_heybox_id

# 设备ID
DEVICE_ID=your_device_id

# 轮询间隔（秒）
POLL_INTERVAL=10
```

## 快速开始

### 启动机器人

```bash
cd src/main
python bot.py
```

### 发送消息示例

```python
from Message.builder import MessageBuilder
from Net.builder import SendMessageReqBuilder

# 创建消息
msg = MessageBuilder()
msg.text("你好").link_id(123456).root_id(-1).reply_id(-1)

# 发送消息
sender = SendMessageReqBuilder("https://api.xiaoheihe.cn/bbs/app/comment/create")
sender.send(msg)
```

### 事件监听

```python
from Event.dispatcher import on
from Event.events import EventAt

@on("at")
def handleAt(event: EventAt):
    print(f"收到@消息: {event.message_id}")
    # 处理逻辑...
```

## 核心模块说明

### Event 模块

| 事件类型 | 说明 |
|----------|------|
| `EventAt` | 收到@消息时触发 |

### Utils 模块

| 工具类 | 说明 |
|--------|------|
| `keygen.py` | 生成 API 请求签名 |
| `check.py` | 环境变量和 Cookie 检查 |
| `dedup.py` | 消息去重处理 |

### Net 模块

| 类 | 说明 |
|----|------|
| `SendMessageReqBuilder` | 发送消息请求构建器 |
| `PollerReqBuilder` | 轮询请求构建器 |

## API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/bbs/app/comment/create` | POST | 发送评论 |
| `/bbs/app/user/message` | GET | 获取消息列表 |

## 注意事项

1. ⚠️ 请妥善保管你的 Cookie，避免泄露
2. ⚠️ 使用本工具请遵守小黑盒社区规定
3. ⚠️ 请勿进行高频请求，避免账号被封禁
4. ⚠️ 建议设置合理的轮询间隔（10秒以上）

## License

MIT License