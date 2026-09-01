Prompts Bot (Flask)

This small scaffold provides a minimal Flask HTTP API for browsing and searching the prompts indexed in zetalib_prompts_index.json.

Endpoints
- GET /health -> {status, count}
- GET /prompts?q=term&category=Category -> list of prompts matching query (searches path+excerpt+category)
- GET /prompts/<id> -> full content and metadata for a prompt (id from /prompts)

Quick start
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. export FLASK_APP=bot.app
5. flask run --host=0.0.0.0 --port=5000

Notes
- The app reads zetalib_prompts_index.json created earlier. Re-generate the index if you add files.
- For production, add pagination, input sanitization, and caching.
