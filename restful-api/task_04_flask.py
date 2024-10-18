#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """
    Handle the root URL and return a welcome message.
    """
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    """
    Handle the /status URL and return 'OK' to indicate the server is running.
    """
    return "OK"

@app.route('/data')
def get_usernames():
    """
    Handle the /data URL and return a JSON list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    """
    Handle the /users/<username> URL and return the user details for the given username.
    If the user is not found, return an error message with a 404 status code.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handle the /add_user URL and accept POST requests to add a new user.
    Parse the incoming JSON data and add the new user to the users dictionary.
    Return a confirmation message with the added user's data or an error message if the username is missing or already exists.
    """
    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = user_data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
