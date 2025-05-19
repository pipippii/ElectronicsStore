from flask import Blueprint, request, jsonify
from PIL import Image
import imagehash
import sqlite3
import os

search = Blueprint('search', __name__)

@search.route('/api/image-search', methods=['POST'])
def image_search():
    uploaded_file = request.files['image']
    img = Image.open(uploaded_file.stream).convert('RGB')
    uploaded_hash = imagehash.average_hash(img)

    conn = sqlite3.connect('backend/database/shop.db')
    c = conn.cursor()
    c.execute("SELECT id, name, image_hash, image_url FROM products")
    products = c.fetchall()

    results = []
    for prod in products:
        stored_hash = imagehash.hex_to_hash(prod[2])
        distance = uploaded_hash - stored_hash
        if distance < 10:  # порог чувствительности
            results.append({
                'id': prod[0],
                'name': prod[1],
                'image_url': prod[3]
            })
    return jsonify(results)