from flask import Blueprint, jsonify
import sqlite3

analytics = Blueprint('analytics', __name__)

@analytics.route('/api/analytics')
def sales_analytics():
    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM orders")
    total_orders = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]
    return jsonify({
        'total_orders': total_orders,
        'total_users': total_users
    })