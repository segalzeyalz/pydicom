from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'store',
        'items': [
            {'name': 'item',
             'price': 15.99
             }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    print(request.get_json())
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_date = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_date['name'],
                'price': request_date['price']
            }
            store['items'].append(new_item)
    return {'messages': 'this store is not found'}


@app.route('/store/<string:name>/item')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return store['items']
    return {'messages': 'this store is not found'}


@app.route('/store/')
def get_stores():
    return jsonify({'stores': stores})


app.run(port=5000)
