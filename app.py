from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'data/snippets.json'

def load_snippets():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_snippets(snippets):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(snippets, f, indent=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    snippets = load_snippets()
    
    if request.method == 'POST':
        command = request.form['command']
        description = request.form['description']
        tags = request.form.get('tags', '').split(',')
        
        snippet = {
            'id': len(snippets) + 1,
            'command': command.strip(),
            'description': description.strip(),
            'tags': [tag.strip() for tag in tags if tag.strip()],
            'created': datetime.now().isoformat()
        }
        snippets.append(snippet)
        save_snippets(snippets)
    
    q = request.args.get('q', '').lower()
    filtered = [s for s in snippets if q in s['command'].lower() or q in s['description'].lower()]
    
    return render_template('index.html', snippets=filtered, q=q)

@app.route('/snippet/<int:sid>')
def snippet_detail(sid):
    snippets = load_snippets()
    snippet = next((s for s in snippets if s['id'] == sid), None)
    if snippet:
        return render_template('detail.html', snippet=snippet)
    return 'Snippet not found', 404

if __name__ == '__main__':
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
