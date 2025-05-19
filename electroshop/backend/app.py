from orders import orders as orders_blueprint
from filters import filters as filters_blueprint
from analytics import analytics as analytics_blueprint

app.register_blueprint(orders_blueprint)
app.register_blueprint(filters_blueprint)
app.register_blueprint(analytics_blueprint)

app = Flask(__name__)
init_db()

@app.route('/api/products')
def api_products():
    return jsonify(get_products())

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/product/<int:product_id>')
def api_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify({
            'id': product[0],
            'name': product[1],
            'price': product[2],
            'description': product[3] if len(product) > 3 else ''
        })
    return jsonify({'error': 'Not found'}), 404


