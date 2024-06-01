#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for the root URL
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route to return JSON data
@app.route('/data')
def data():
    return jsonify(list(users.keys()))

# Route to return status
@app.route('/status')
def status():
    return "OK"

# Route to return user data based on username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username or username in users:
        return jsonify({"error": "Invalid username or user already exists"}), 400
    
    user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
