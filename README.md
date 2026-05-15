# Heybox Core

小黑盒机器人核心框架 - 基于 Python | Heybox Bot Core Framework

## 项目简介

Heybox Core 是一个功能完整的小黑盒（Heybox）社区机器人开发框架，提供消息监听、事件分发、自动回复、登录认证等核心功能。

## 功能特性

- ✅ 请求签名生成（hkey、nonce、timestamp）
- ✅ 消息轮询与事件分发系统
- ✅ @消息自动回复功能
- ✅ 消息去重机制（基于文件缓存）
- ✅ Cookie 有效期检测
- ✅ 完整的日志系统
- ✅ 二维码登录支持

## 项目结构

```
heybox-core/
├── src/
│   ├── main/                    # 主程序目录
│   │   ├── Event/              # 事件系统
│   │   │   ├── dispatcher.py   # 事件分发器（注册/触发事件）
│   │   │   └── events.py       # 事件定义（EventAt）
│   │   ├── Log/                # 日志模块
│   │   │   ├── __init__.py
│   │   │   └── logger.py       # 日志配置与初始化
│   │   ├── Login/              # 登录模块
│   │   │   ├── __init__.py
│   │   │   └── login.py        # 二维码登录逻辑
│   │   ├── Message/            # 消息构建
│   │   │   ├── __init__.py
│   │   │   └── builder.py      # 消息构建器（链式调用）
│   │   ├── Net/                # 网络请求
│   │   │   ├── __init__.py
│   │   │   └── builder.py      # 请求构建器（签名自动生成）
│   │   ├── Utils/              # 工具类
│   │   │   ├── __init__.py
│   │   │   ├── check.py        # 环境变量和Cookie检查
│   │   │   ├── dedup.py        # 消息去重处理器
│   │   │   ├── error.py        # 自定义错误类
│   │   │   └── keygen.py       # 签名生成工具
│   │   ├── caches/             # 缓存目录
│   │   │   └── msg/            # 消息缓存
│   │   │       └── dedup.json  # 去重记录文件
│   │   ├── bot.py              # 机器人主入口
│   │   ├── poller.py           # 消息轮询器
│   │   └── test.py             # 测试脚本
│   ├── encoder_cli/            # JavaScript加密逻辑
│   │   └── process_origin.js   # 签名生成核心算法
│   ├── note/                   # 备注文件
│   │   └── note_response.txt   # API响应示例
│   └── test/                   # 单元测试
│       ├── AtGetTest.py        # @消息获取测试
│       ├── GetQrCodeState.py   # 二维码状态查询测试
│       ├── GetQrCodeTest.py    # 二维码获取测试
│       ├── GetSendTokenTest.py # 签名生成测试
│       └── SendMessageTest.py  # 消息发送测试
├── .gitignore
├── LICENSE
└── README.md
```

## 环境要求

- Python 3.8+
- Node.js（用于执行 JavaScript 加密逻辑）

## 安装依赖

```bash
pip install requests python-dotenv PyExecJS qrcode
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
    print(f"用户: {event.user_name}")
    print(f"内容: {event.addition_text}")
    # 处理逻辑...
```

### 二维码登录

```python
from Login.login import do_login

# 执行二维码登录
do_login()
# 登录成功后会自动保存Cookie到.env文件
```

**登录流程**：
1. 调用 `/account/get_qrcode_url/` 获取二维码URL
2. 在终端打印ASCII二维码
3. 用户使用小黑盒APP扫描二维码
4. 轮询 `/account/qr_state/` 检查登录状态
5. 登录成功后自动提取Cookie并保存到 `.env` 文件

**登录状态说明**：

| 状态 | 说明 |
|------|------|
| `wait` | 等待扫码 |
| `ready` | 已扫码，等待确认 |
| `cancel` | 用户取消登录 |
| `ok` | 登录成功 |

## 核心模块说明

### Event 模块

| 文件              | 说明                   |
| --------------- | -------------------- |
| `dispatcher.py` | 事件分发器，支持注册和触发事件      |
| `events.py`     | 事件定义类，当前支持 `EventAt` |

**EventAt 属性**：

| 属性              | 类型  | 说明    |
| --------------- | --- | ----- |
| `event_type`    | str | 事件类型  |
| `message_id`    | str | 消息ID  |
| `addition_text` | str | @消息内容 |
| `post_title`    | str | 帖子标题  |
| `link_id`       | str | 帖子ID  |
| `root_id`       | str | 根评论ID |
| `user_id`       | str | 用户ID  |
| `user_name`     | str | 用户名   |
| `time_stamp`    | int | 时间戳   |

### Net 模块

| 类                       | 说明         |
| ----------------------- | ---------- |
| `ReqBuilder`            | 基础请求构建器    |
| `QrCodeReqBuilder`      | 二维码请求构建器   |
| `GetQrStatusReqBuilder` | 二维码状态查询构建器 |
| `SendMessageReqBuilder` | 发送消息请求构建器  |
| `PollerReqBuilder`      | 轮询请求构建器    |

### Utils 模块

| 文件          | 说明                           |
| ----------- | ---------------------------- |
| `keygen.py` | 生成 API 请求签名（hkey/nonce/time） |
| `check.py`  | 环境变量和 Cookie 有效性检查           |
| `dedup.py`  | 消息去重处理（基于文件缓存）               |
| `error.py`  | 自定义错误类定义                     |

### Login 模块

| 文件         | 说明      |
| ---------- | ------- |
| `login.py` | 二维码登录逻辑（生成二维码、轮询状态、保存Cookie） |

**Login 模块方法**：

| 方法 | 说明 | 参数 | 返回值 |
|------|------|------|--------|
| `generate_qr_code()` | 生成二维码并返回ID | 无 | `qr_code_id` (str) |
| `get_qr_code_status(qr_code_id)` | 查询二维码状态 | `qr_code_id`: 二维码ID | 请求对象 |
| `do_login()` | 执行完整登录流程 | 无 | 无（自动保存Cookie） |

## API 接口

| 接口                        | 方法   | 说明     |
| ------------------------- | ---- | ------ |
| `/bbs/app/comment/create` | POST | 发送评论   |
| `/bbs/app/user/message`   | GET  | 获取消息列表 |
| `/account/get_qrcode_url/`| POST | 获取二维码URL |
| `/account/qr_state/`      | GET  | 查询二维码状态 |

## 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                       bot.py (主入口)                        │
└─────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   Poller      │    │  Event        │    │   Logger      │
│  (消息轮询)    │    │  Dispatcher   │    │  (日志系统)    │
└───────────────┘    └───────────────┘    └───────────────┘
         │                    │
         ▼                    ▼
┌───────────────┐    ┌───────────────┐
│   Net         │    │   Message     │
│  (网络请求)    │    │  Builder      │
└───────────────┘    └───────────────┘
         │
         ▼
┌───────────────┐
│   Utils       │
│ (工具类:签名/检查/去重) │
└───────────────┘
```

## 注意事项

1. ⚠️ 请妥善保管你的 Cookie，避免泄露
2. ⚠️ 使用本工具请遵守小黑盒社区规定
3. ⚠️ 请勿进行高频请求，避免账号被封禁
4. ⚠️ 建议设置合理的轮询间隔（10秒以上）
5. ⚠️ 定期检查 Cookie 有效期

## License

MIT License
