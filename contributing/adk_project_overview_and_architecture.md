# ADK Project Overview and Architecture
ADK 项目概述和架构

Google Agent Development Kit (ADK) for Python

## Core Philosophy & Architecture
核心理念与架构

- Code-First: Everything is defined in Python code for versioning, testing, and IDE support. Avoid GUI-based logic.
  代码优先: 所有内容都用 Python 代码定义, 以便进行版本控制、测试和 IDE 支持. 避免使用基于 GUI 的逻辑.

- Modularity & Composition: We build complex multi-agent systems by composing multiple, smaller, specialized agents.
  模块化与组合: 我们通过组合多个较小的、专门化的智能体来构建复杂的多智能体系统.

- Deployment-Agnostic: The agent's core logic is separate from its deployment environment. The same agent.py can be run locally for testing, served via an API, or deployed to the cloud.
  部署方式无关: 代理的核心逻辑与其部署环境分离. 同一个 agent.py 文件既可以在本地运行进行测试, 也可以通过 API 提供服务, 或者部署到云端.

## Foundational Abstractions (Our Vocabulary)
基础抽象概念(我们的词汇)

- Agent: The blueprint. It defines an agent's identity, instructions, and tools. It's a declarative configuration object.
  代理: 蓝图. 它定义了代理的身份、指令和工具. 它是一个声明式配置对象.

- Tool: A capability. A Python function an agent can call to interact with the world (e.g., search, API call).
  工具: 一种功能. 代理可以调用​​ Python 函数来与外部世界交互(例如, 搜索、API 调用).

- Runner: The engine. It orchestrates the "Reason-Act" loop, manages LLM calls, and executes tools.
  运行器: 引擎. 它负责协调"推理-行动"循环, 管理 LLM 调用, 并执行工具.

- Session: The conversation state. It holds the history for a single, continuous dialogue.
  会话: 对话状态. 它保存着一次连续对话的历史记录.

- Memory: Long-term recall across different sessions.
  记忆力: 跨不同会话的长期回忆能力.

- Artifact Service: Manages non-textual data like files.
  Artifact Service: 管理非文本数据, 例如文件.

## Canonical Project Structure
规范项目结构

Adhere to this structure for compatibility with ADK tooling.
为了与 ADK 工具兼容, 请遵循此结构.

```
my_adk_project/
└── src/
    └── my_app/
        ├── agents/
        │   ├── my_agent/
        │   │   ├── __init__.py   # Must contain: from . import agent \
        │   │   └── agent.py      # Must contain: root_agent = Agent(...) \
        │   └── another_agent/
        │       ├── __init__.py
        │       └── agent.py\
```

agent.py: Must define the agent and assign it to a variable named root_agent. This is how ADK's tools find it.
agent.py: 必须定义代理并将其赋值给名为 root_agent 的变量. ADK 的工具就是通过这种方式找到它的.

`__init__.py`: In each agent directory, it must contain `from . import agent` to make the agent discoverable.
`__init__.py` : 在每个代理目录中, 它必须包含 `from . import agent`, 以使代理可被发现.

## Local Development & Debugging
本地开发与调试

Interactive UI (adk web): This is our primary debugging tool. It's a decoupled system:
交互式用户界面(ADK Web): 这是我们的主要调试工具. 它是一个解耦系统:

Backend: A FastAPI server started with adk api_server.
后端: 使用 adk api_server 启动的 FastAPI 服务器.

Frontend: An Angular app that connects to the backend.
前端: 一个连接到后端的 Angular 应用.

Use the "Events" tab to inspect the full execution trace (prompts, tool calls, responses).
使用"事件"选项卡检查完整的执行跟踪(提示、工具调用、响应).

CLI (adk run): For quick, stateless functional checks in the terminal.
CLI(adk run): 用于在终端中快速、无状态的功能检查.

Programmatic (pytest): For writing automated unit and integration tests.
程序化(pytest): 用于编写自动化单元测试和集成测试.

## The API Layer (FastAPI)

We expose agents as production APIs using FastAPI.
我们使用 FastAPI 将代理作为生产 API 公开.

- get_fast_api_app: This is the key helper function from google.adk.cli.fast_api that creates a FastAPI app from our agent directory.
  get_fast_api_app: 这是 google.adk.cli.fast_api 中的关键辅助函数, 它从我们的代理目录创建一个 FastAPI 应用.

- Standard Endpoints: The generated app includes standard routes like /list-apps and /run_sse for streaming responses. The wire format is camelCase.
  标准端点: 生成的应用程序包含诸如 /list-apps 和 /run_sse 之类的标准路由, 用于流式响应. 网络接口格式为驼峰式命名法 (camelCase).

- Custom Endpoints: We can add our own routes (e.g., /health) to the app object returned by the helper.
  自定义端点: 我们可以向辅助函数返回的应用程序对象添加我们自己的路由(例如, /health).

```Python

from google.adk.cli.fast_api import get_fast_api_app
app = get_fast_api_app(agent_dir="./agents")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
```


## Deployment to Production

The adk cli provides the "adk deploy" command to deploy to Google Vertex Agent Engine, Google CloudRun, Google GKE.
adk cli 提供"adk deploy"命令, 用于部署到 Google Vertex Agent Engine、Google CloudRun 和 Google GKE.

## Testing & Evaluation Strategy
测试与评估策略

Testing is layered, like a pyramid.
测试是一个分层的过程, 就像金字塔一样.

### Layer 1: Unit Tests (Base)
第一层: 单元测试(基础)

What: Test individual Tool functions in isolation.
内容: 单独测试工具的各个功能.

How: Use pytest in tests/test_tools.py. Verify deterministic logic.
方法: 在 tests/test_tools.py 中使用 pytest. 验证确定性逻辑.

### Layer 2: Integration Tests (Middle)
第二层: 集成测试(中间层)

What: Test the agent's internal logic and interaction with tools.
内容: 测试代理的内部逻辑以及与工具的交互.

How: Use pytest in tests/test_agent.py, often with mocked LLMs or services.
方法: 在 tests/test_agent.py 中使用 pytest, 通常使用模拟的 LLM 或服务.

### Layer 3: Evaluation Tests (Top)
第三层: 评估测试(顶部)

What: Assess end-to-end performance with a live LLM. This is about quality, not just pass/fail.
内容: 使用实时生命周期管理 (LLM) 评估端到端性能. 这关乎质量, 而不仅仅是合格/不合格.

How: Use the ADK Evaluation Framework.
方法: 使用 ADK 评估框架.

Test Cases: Create JSON files with input and a reference (expected tool calls and final response).
测试用例: 创建包含输入和参考(预期工具调用和最终响应)的 JSON 文件.

Metrics: tool_trajectory_avg_score (does it use tools correctly?) and response_match_score (is the final answer good?).
指标: tool_trajectory_avg_score(是否正确使用工具?)和 response_match_score(最终答案是否良好?).

Run via: adk web (UI), pytest (for CI/CD), or adk eval (CLI).
运行方式: adk web(UI)、pytest(用于 CI/CD)或 adk eval(CLI).
