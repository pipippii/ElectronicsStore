from flask import Blueprint, request, jsonify
import sqlite3

filters = Blueprint('filters', __name__)

@filters.route('/api/filter')
def filter_products():
    price_range = request.args.get('price', '')
    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    query = "SELECT id, name, image_url FROM products"

    if price_range:
        if '+' in price_range:
            price_min = int(price_range.replace('+', ''))
            query += f" WHERE price >= {price_min}"
        elif '-' in price_range:
            min_price, max_price = map(int, price_range.split('-'))
            query += f" WHERE price BETWEEN {min_price} AND {max_price}"

    c.execute(query)
    products = c.fetchall()
    return jsonify([{ 'id': p[0], 'name': p[1], 'image_url': p[2] } for p in products])