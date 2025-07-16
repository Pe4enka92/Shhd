from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

DATA_FILE = 'data.json'

# Инициализация файла данных
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({
            "juices": [
                {"name": "🍓🍦 Strawberry ice cream", "available": True},
                {"name": "🍑 peach ice", "available": True},
                {"name": "🥝Kiwi and Guava", "available": True},
                {"name": "🍋Perfumе lemon", "available": True},
                {"name": "🔥Lava fire", "available": True},
                {"name": "🍉 watermelon bubblegum", "available": True},
                {"name": "🥶Mint ice", "available": True},
                {"name": "🍉🫐blueberry watermelon", "available": True},
                {"name": "🤩🍹Pomegranate lemonade", "available": True}
            ]
        }, f)

def read_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/api/juices')
def get_juices():
    data = read_data()
    return jsonify(data['juices'])

@app.route('/api/update', methods=['POST'])
def update_availability():
    if request.json.get("admin_user") != "@duxcrime" or request.json.get("admin_pass") != "duxcrime":
        return jsonify({"error": "Unauthorized"}), 403
    name = request.json.get("name")
    available = request.json.get("available")
    data = read_data()
    for juice in data['juices']:
        if juice['name'] == name:
            juice['available'] = available
    write_data(data)
    return jsonify({"success": True})

@app.route('/api/add', methods=['POST'])
def add_juice():
    if request.json.get("admin_user") != "@duxcrime" or request.json.get("admin_pass") != "duxcrime":
        return jsonify({"error": "Unauthorized"}), 403
    new_name = request.json.get("name")
    data = read_data()
    data['juices'].append({"name": new_name, "available": True})
    write_data(data)
    return jsonify({"success": True})

@app.route('/api/delete', methods=['POST'])
def delete_juice():
    if request.json.get("admin_user") != "@duxcrime" or request.json.get("admin_pass") != "duxcrime":
        return jsonify({"error": "Unauthorized"}), 403
    name = request.json.get("name")
    data = read_data()
    data['juices'] = [j for j in data['juices'] if j['name'] != name]
    write_data(data)
    return jsonify({"success": True})

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
