from flask import Flask, jsonify, request, abort
import json
import os

app = Flask(__name__)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INDEX_PATH = os.path.join(ROOT, 'zetalib_prompts_index.json')

try:
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        INDEX = json.load(f)
except Exception:
    INDEX = []

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'count': len(INDEX)})

@app.route('/prompts')
def list_prompts():
    q = (request.args.get('q') or '').lower()
    category = request.args.get('category')
    results = []
    for i, item in enumerate(INDEX):
        if category and item.get('category') != category:
            continue
        if q:
            hay = ' '.join([item.get('path',''), item.get('excerpt',''), item.get('category','')]).lower()
            if q not in hay:
                continue
        results.append({
            'id': i,
            'path': item.get('path'),
            'category': item.get('category'),
            'excerpt': item.get('excerpt'),
        })
    return jsonify(results)

@app.route('/prompts/<int:pid>')
def get_prompt(pid):
    if pid < 0 or pid >= len(INDEX):
        abort(404)
    item = INDEX[pid]
    file_path = os.path.join(ROOT, item['path'])
    content = ''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        content = ''
    return jsonify({
        'id': pid,
        'path': item['path'],
        'category': item['category'],
        'excerpt': item['excerpt'],
        'content': content,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
