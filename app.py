from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

FLAVOR_FILE = 'flavors.json'

def load_flavors():
    if not os.path.exists(FLAVOR_FILE):
        with open(FLAVOR_FILE, 'w') as f:
            json.dump([], f)
    with open(FLAVOR_FILE, 'r') as f:
        return json.load(f)

def save_flavors(data):
    with open(FLAVOR_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/api/flavors', methods=['GET'])
def get_flavors():
    return jsonify(load_flavors())

@app.route('/api/flavors', methods=['POST'])
def add_flavor():
    flavor = request.json.get('flavor')
    data = load_flavors()
    data.append(flavor)
    save_flavors(data)
    return jsonify({'status': 'ok'})

@app.route('/api/flavors/<int:index>', methods=['DELETE'])
def delete_flavor(index):
    data = load_flavors()
    if 0 <= index < len(data):
        data.pop(index)
        save_flavors(data)
        return jsonify({'status': 'deleted'})
    return jsonify({'error': 'invalid index'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
