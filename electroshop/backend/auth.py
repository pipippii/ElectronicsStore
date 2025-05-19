from flask import Blueprint, request, jsonify
import sqlite3
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = "your-secret"
auth = Blueprint('auth', __name__)

@auth.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = generate_password_hash(data['password'])

    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    return jsonify({'message': 'User registered successfully'})

@auth.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    user = c.fetchone()

    if user and check_password_hash(user[2], password):
        token = jwt.encode({
            'user_id': user[0],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid credentials'}), 401