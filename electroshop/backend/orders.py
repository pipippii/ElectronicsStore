from flask import Blueprint, request, jsonify
import sqlite3
import json

orders = Blueprint('orders', __name__)

@orders.route('/api/order', methods=['POST'])
def place_order():
    data = request.get_json()
    user_id = data['user_id']
    items = json.dumps(data['items'])

    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders (user_id, items) VALUES (?, ?)", (user_id, items))
    conn.commit()
    return jsonify({'status': 'success'})
