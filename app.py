
from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

ADMIN_USER = "@duxcrime"
ADMIN_PASS = "duxcrime"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"juices": []}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", juices=data["juices"])

@app.route("/update", methods=["POST"])
def update():
    user = request.form.get("user")
    password = request.form.get("pass")
    if user != ADMIN_USER or password != ADMIN_PASS:
        return "Unauthorized", 403

    data = load_data()
    name = request.form.get("name")
    action = request.form.get("action")

    if action == "add":
        data["juices"].append({"name": name, "available": True})
    elif action == "delete":
        data["juices"] = [j for j in data["juices"] if j["name"] != name]
    elif action == "toggle":
        for juice in data["juices"]:
            if juice["name"] == name:
                juice["available"] = not juice["available"]
                break

    save_data(data)
    return redirect("/")

@app.route("/data")
def get_data():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True)
