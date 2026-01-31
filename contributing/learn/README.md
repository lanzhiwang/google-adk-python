# 环境准备


```bash
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda env list
conda create --name adk python=3.12 -y
conda activate adk
conda deactivate
conda env remove -n adk -y

# 调试时选择 python 解释器
Python: Select Interpreter

pip -v install uv==0.9.28 -i https://pypi.tuna.tsinghua.edu.cn/simple

uv pip -v install --index https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple google-adk==1.23.0 litellm==1.81.5


$ mkdir adk
$ cd adk
$ pwd
/root/adk
$ adk create my_agent
Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 2

Please see below guide to configure other models:
https://google.github.io/adk-docs/agents/models


Agent created in /root/adk/my_agent:
- .env
- __init__.py
- agent.py

$ tree -a my_agent/
my_agent/
├── .env
├── __init__.py
└── agent.py

0 directories, 3 files
$


(adk) root@k8s-a40-node02:~/adk# export OLLAMA_API_BASE="http://localhost:11434"
(adk) root@k8s-a40-node02:~/adk# echo ${OLLAMA_API_BASE}
http://localhost:11434
(adk) root@k8s-a40-node02:~/adk# adk web --host=0.0.0.0 --port=8000 --log_level=debug
2026-01-31 15:20:02,466 - DEBUG - service_registry.py:206 - services.py not found in /root/adk, skipping.
2026-01-31 15:20:02,467 - INFO - service_factory.py:266 - Using in-memory memory service
2026-01-31 15:20:02,467 - INFO - local_storage.py:83 - Using per-agent session storage rooted at /root/adk
2026-01-31 15:20:02,467 - INFO - local_storage.py:109 - Using file artifact service at /root/adk/.adk/artifacts
/root/anaconda3/envs/adk/lib/python3.12/site-packages/google/adk/cli/fast_api.py:141: UserWarning: [EXPERIMENTAL] InMemoryCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  credential_service = InMemoryCredentialService()
/root/anaconda3/envs/adk/lib/python3.12/site-packages/google/adk/auth/credential_service/in_memory_credential_service.py:33: UserWarning: [EXPERIMENTAL] BaseCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__()
2026-01-31 15:20:02,577 - DEBUG - selector_events.py:64 - Using selector: EpollSelector
INFO:     Started server process [3062087]
INFO:     Waiting for application startup.

+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://0.0.0.0:8000.                         |
+-----------------------------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     172.16.64.195:64405 - "GET / HTTP/1.1" 307 Temporary Redirect
INFO:     172.16.64.195:64405 - "GET /dev-ui/ HTTP/1.1" 304 Not Modified
INFO:     172.16.64.195:64405 - "GET /dev-ui/chunk-2WH2EVR6.js HTTP/1.1" 304 Not Modified
INFO:     172.16.64.195:64404 - "GET /dev-ui/polyfills-B6TNHZQ6.js HTTP/1.1" 304 Not Modified
INFO:     172.16.64.195:64405 - "GET /dev-ui/main-MTHA237R.js HTTP/1.1" 304 Not Modified
INFO:     172.16.64.195:64405 - "GET /dev-ui/styles-SCBTF4PF.css HTTP/1.1" 304 Not Modified
INFO:     172.16.64.195:64405 - "GET /dev-ui/assets/config/runtime-config.json HTTP/1.1" 200 OK
INFO:     172.16.64.195:64405 - "GET /list-apps?relative_path=./ HTTP/1.1" 200 OK
INFO:     172.16.64.195:64405 - "GET /dev-ui/assets/ADK-512-color.svg HTTP/1.1" 304 Not Modified
INFO:     172.16.64.195:64404 - "GET /builder/app/my_agent?ts=1769844079928 HTTP/1.1" 200 OK
2026-01-31 15:21:20,136 - INFO - local_storage.py:59 - Creating local session service at /root/adk/my_agent/.adk/session.db
2026-01-31 15:21:20,138 - DEBUG - core.py:62 - executing <function connect.<locals>.connector at 0x7f4487f8d120>
2026-01-31 15:21:20,139 - DEBUG - core.py:67 - operation <function connect.<locals>.connector at 0x7f4487f8d120> completed
2026-01-31 15:21:20,139 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'PRAGMA foreign_keys = ON', [])
2026-01-31 15:21:20,139 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'PRAGMA foreign_keys = ON', []) completed
2026-01-31 15:21:20,139 - DEBUG - core.py:62 - executing functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487facc70>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n')
2026-01-31 15:21:20,140 - DEBUG - core.py:67 - operation functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487facc70>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n') completed
2026-01-31 15:21:20,140 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'SELECT 1 FROM sessions WHERE app_name=? AND user_id=? AND id=?', ('my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f'))
2026-01-31 15:21:20,140 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'SELECT 1 FROM sessions WHERE app_name=? AND user_id=? AND id=?', ('my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f')) completed
2026-01-31 15:21:20,140 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0c40>)
2026-01-31 15:21:20,140 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0c40>) completed
2026-01-31 15:21:20,140 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0c40>)
2026-01-31 15:21:20,140 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0c40>) completed
2026-01-31 15:21:20,141 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',))
2026-01-31 15:21:20,141 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',)) completed
2026-01-31 15:21:20,141 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0dc0>)
2026-01-31 15:21:20,141 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0dc0>) completed
2026-01-31 15:21:20,141 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0dc0>)
2026-01-31 15:21:20,141 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0dc0>) completed
2026-01-31 15:21:20,141 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user'))
2026-01-31 15:21:20,142 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user')) completed
2026-01-31 15:21:20,142 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0dc0>)
2026-01-31 15:21:20,142 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0dc0>) completed
2026-01-31 15:21:20,142 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0dc0>)
2026-01-31 15:21:20,142 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0dc0>) completed
2026-01-31 15:21:20,142 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, '\n          INSERT INTO sessions (app_name, user_id, id, state, create_time, update_time)\n          VALUES (?, ?, ?, ?, ?, ?)\n          ', ('my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f', '{}', 1769844080.1380007, 1769844080.1380007))
2026-01-31 15:21:20,142 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487facc70>, '\n          INSERT INTO sessions (app_name, user_id, id, state, create_time, update_time)\n          VALUES (?, ?, ?, ?, ?, ?)\n          ', ('my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f', '{}', 1769844080.1380007, 1769844080.1380007)) completed
2026-01-31 15:21:20,143 - DEBUG - core.py:62 - executing functools.partial(<built-in method commit of sqlite3.Connection object at 0x7f4487facc70>)
2026-01-31 15:21:20,144 - DEBUG - core.py:67 - operation functools.partial(<built-in method commit of sqlite3.Connection object at 0x7f4487facc70>) completed
2026-01-31 15:21:20,144 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487facc70>)
2026-01-31 15:21:20,144 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487facc70>) completed
2026-01-31 15:21:20,145 - DEBUG - core.py:62 - executing <function Connection.stop.<locals>.close_and_stop at 0x7f4487f8cc20>
2026-01-31 15:21:20,145 - DEBUG - core.py:67 - operation <function Connection.stop.<locals>.close_and_stop at 0x7f4487f8cc20> completed
2026-01-31 15:21:20,145 - INFO - adk_web_server.py:660 - New session created: cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f
INFO:     172.16.64.195:64405 - "POST /apps/my_agent/users/user/sessions HTTP/1.1" 200 OK
2026-01-31 15:21:20,329 - DEBUG - core.py:62 - executing <function connect.<locals>.connector at 0x7f4487f8ce00>
2026-01-31 15:21:20,329 - DEBUG - core.py:67 - operation <function connect.<locals>.connector at 0x7f4487f8ce00> completed
2026-01-31 15:21:20,330 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'PRAGMA foreign_keys = ON', [])
2026-01-31 15:21:20,330 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'PRAGMA foreign_keys = ON', []) completed
2026-01-31 15:21:20,330 - DEBUG - core.py:62 - executing functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487fad030>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n')
2026-01-31 15:21:20,330 - DEBUG - core.py:67 - operation functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487fad030>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n') completed
2026-01-31 15:21:20,330 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state, update_time FROM sessions WHERE app_name=? AND user_id=? AND id=?', ('my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f'))
2026-01-31 15:21:20,330 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state, update_time FROM sessions WHERE app_name=? AND user_id=? AND id=?', ('my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f')) completed
2026-01-31 15:21:20,331 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0ec0>)
2026-01-31 15:21:20,331 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0ec0>) completed
2026-01-31 15:21:20,331 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0ec0>)
2026-01-31 15:21:20,331 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0ec0>) completed
2026-01-31 15:21:20,331 - DEBUG - core.py:62 - executing functools.partial(<bound method Connection._execute_fetchall of <aiosqlite.core.Connection object at 0x7f4487f675f0>>, 'SELECT event_data FROM events WHERE app_name=? AND user_id=? AND session_id=? ORDER BY timestamp DESC', ['my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f'])
2026-01-31 15:21:20,331 - DEBUG - core.py:67 - operation functools.partial(<bound method Connection._execute_fetchall of <aiosqlite.core.Connection object at 0x7f4487f675f0>>, 'SELECT event_data FROM events WHERE app_name=? AND user_id=? AND session_id=? ORDER BY timestamp DESC', ['my_agent', 'user', 'cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f']) completed
2026-01-31 15:21:20,331 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',))
2026-01-31 15:21:20,331 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',)) completed
2026-01-31 15:21:20,331 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0f40>)
2026-01-31 15:21:20,332 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0f40>) completed
2026-01-31 15:21:20,332 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0f40>)
2026-01-31 15:21:20,332 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0f40>) completed
2026-01-31 15:21:20,332 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user'))
2026-01-31 15:21:20,332 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user')) completed
2026-01-31 15:21:20,332 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0f40>)
2026-01-31 15:21:20,332 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa0f40>) completed
2026-01-31 15:21:20,332 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0f40>)
2026-01-31 15:21:20,332 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa0f40>) completed
2026-01-31 15:21:20,332 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487fad030>)
2026-01-31 15:21:20,333 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487fad030>) completed
2026-01-31 15:21:20,333 - DEBUG - core.py:62 - executing <function Connection.stop.<locals>.close_and_stop at 0x7f4487f2ab60>
2026-01-31 15:21:20,333 - DEBUG - core.py:67 - operation <function Connection.stop.<locals>.close_and_stop at 0x7f4487f2ab60> completed
INFO:     172.16.64.195:64405 - "GET /apps/my_agent/users/user/sessions/cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f HTTP/1.1" 200 OK
INFO:     172.16.64.195:64405 - "GET /debug/trace/session/cf1b1ca6-0a4a-45af-abdd-d31f4eb4cd0f HTTP/1.1" 200 OK
2026-01-31 15:21:20,492 - DEBUG - core.py:62 - executing <function connect.<locals>.connector at 0x7f4487f8cc20>
2026-01-31 15:21:20,492 - DEBUG - core.py:67 - operation <function connect.<locals>.connector at 0x7f4487f8cc20> completed
2026-01-31 15:21:20,492 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'PRAGMA foreign_keys = ON', [])
2026-01-31 15:21:20,492 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'PRAGMA foreign_keys = ON', []) completed
2026-01-31 15:21:20,493 - DEBUG - core.py:62 - executing functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487fad030>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n')
2026-01-31 15:21:20,493 - DEBUG - core.py:67 - operation functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487fad030>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n') completed
2026-01-31 15:21:20,493 - DEBUG - core.py:62 - executing functools.partial(<bound method Connection._execute_fetchall of <aiosqlite.core.Connection object at 0x7f4487f67e30>>, 'SELECT id, user_id, state, update_time FROM sessions WHERE app_name=? AND user_id=?', ('my_agent', 'user'))
2026-01-31 15:21:20,493 - DEBUG - core.py:67 - operation functools.partial(<bound method Connection._execute_fetchall of <aiosqlite.core.Connection object at 0x7f4487f67e30>>, 'SELECT id, user_id, state, update_time FROM sessions WHERE app_name=? AND user_id=?', ('my_agent', 'user')) completed
2026-01-31 15:21:20,493 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',))
2026-01-31 15:21:20,494 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',)) completed
2026-01-31 15:21:20,494 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa1240>)
2026-01-31 15:21:20,494 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa1240>) completed
2026-01-31 15:21:20,494 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa1240>)
2026-01-31 15:21:20,494 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa1240>) completed
2026-01-31 15:21:20,494 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user'))
2026-01-31 15:21:20,494 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user')) completed
2026-01-31 15:21:20,494 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa1240>)
2026-01-31 15:21:20,494 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa1240>) completed
2026-01-31 15:21:20,494 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa1240>)
2026-01-31 15:21:20,494 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa1240>) completed
2026-01-31 15:21:20,495 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487fad030>)
2026-01-31 15:21:20,495 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487fad030>) completed
2026-01-31 15:21:20,495 - DEBUG - core.py:62 - executing <function Connection.stop.<locals>.close_and_stop at 0x7f4492d0ae80>
2026-01-31 15:21:20,495 - DEBUG - core.py:67 - operation <function Connection.stop.<locals>.close_and_stop at 0x7f4492d0ae80> completed
INFO:     172.16.64.195:64405 - "GET /apps/my_agent/users/user/sessions HTTP/1.1" 200 OK
INFO:     172.16.64.195:64404 - "GET /apps/my_agent/eval_results HTTP/1.1" 200 OK
INFO:     172.16.64.195:64405 - "GET /apps/my_agent/eval_sets HTTP/1.1" 200 OK
2026-01-31 15:21:20,621 - DEBUG - core.py:62 - executing <function connect.<locals>.connector at 0x7f4487f8ce00>
2026-01-31 15:21:20,621 - DEBUG - core.py:67 - operation <function connect.<locals>.connector at 0x7f4487f8ce00> completed
2026-01-31 15:21:20,622 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'PRAGMA foreign_keys = ON', [])
2026-01-31 15:21:20,622 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'PRAGMA foreign_keys = ON', []) completed
2026-01-31 15:21:20,622 - DEBUG - core.py:62 - executing functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487fad030>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n')
2026-01-31 15:21:20,622 - DEBUG - core.py:67 - operation functools.partial(<built-in method executescript of sqlite3.Connection object at 0x7f4487fad030>, '\nCREATE TABLE IF NOT EXISTS app_states (\n    app_name TEXT PRIMARY KEY,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL\n);\n\n\nCREATE TABLE IF NOT EXISTS user_states (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id)\n);\n\n\nCREATE TABLE IF NOT EXISTS sessions (\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    id TEXT NOT NULL,\n    state TEXT NOT NULL,\n    create_time REAL NOT NULL,\n    update_time REAL NOT NULL,\n    PRIMARY KEY (app_name, user_id, id)\n);\n\n\nCREATE TABLE IF NOT EXISTS events (\n    id TEXT NOT NULL,\n    app_name TEXT NOT NULL,\n    user_id TEXT NOT NULL,\n    session_id TEXT NOT NULL,\n    invocation_id TEXT NOT NULL,\n    timestamp REAL NOT NULL,\n    event_data TEXT NOT NULL,\n    PRIMARY KEY (app_name, user_id, session_id, id),\n    FOREIGN KEY (app_name, user_id, session_id) REFERENCES sessions(app_name, user_id, id) ON DELETE CASCADE\n);\n') completed
2026-01-31 15:21:20,622 - DEBUG - core.py:62 - executing functools.partial(<bound method Connection._execute_fetchall of <aiosqlite.core.Connection object at 0x7f4487f674d0>>, 'SELECT id, user_id, state, update_time FROM sessions WHERE app_name=? AND user_id=?', ('my_agent', 'user'))
2026-01-31 15:21:20,623 - DEBUG - core.py:67 - operation functools.partial(<bound method Connection._execute_fetchall of <aiosqlite.core.Connection object at 0x7f4487f674d0>>, 'SELECT id, user_id, state, update_time FROM sessions WHERE app_name=? AND user_id=?', ('my_agent', 'user')) completed
2026-01-31 15:21:20,623 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',))
2026-01-31 15:21:20,623 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM app_states WHERE app_name=?', ('my_agent',)) completed
2026-01-31 15:21:20,623 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa19c0>)
2026-01-31 15:21:20,623 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa19c0>) completed
2026-01-31 15:21:20,623 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa19c0>)
2026-01-31 15:21:20,623 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa19c0>) completed
2026-01-31 15:21:20,623 - DEBUG - core.py:62 - executing functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user'))
2026-01-31 15:21:20,623 - DEBUG - core.py:67 - operation functools.partial(<built-in method execute of sqlite3.Connection object at 0x7f4487fad030>, 'SELECT state FROM user_states WHERE app_name=? AND user_id=?', ('my_agent', 'user')) completed
2026-01-31 15:21:20,623 - DEBUG - core.py:62 - executing functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa19c0>)
2026-01-31 15:21:20,624 - DEBUG - core.py:67 - operation functools.partial(<built-in method fetchone of sqlite3.Cursor object at 0x7f4487fa19c0>) completed
2026-01-31 15:21:20,624 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa19c0>)
2026-01-31 15:21:20,624 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Cursor object at 0x7f4487fa19c0>) completed
2026-01-31 15:21:20,624 - DEBUG - core.py:62 - executing functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487fad030>)
2026-01-31 15:21:20,624 - DEBUG - core.py:67 - operation functools.partial(<built-in method close of sqlite3.Connection object at 0x7f4487fad030>) completed
2026-01-31 15:21:20,624 - DEBUG - core.py:62 - executing <function Connection.stop.<locals>.close_and_stop at 0x7f448c985e40>
2026-01-31 15:21:20,624 - DEBUG - core.py:67 - operation <function Connection.stop.<locals>.close_and_stop at 0x7f448c985e40> completed
INFO:     172.16.64.195:64405 - "GET /apps/my_agent/users/user/sessions HTTP/1.1" 200 OK


```
