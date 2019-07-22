from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {'name': 'item',
             'price': 15.99
             }
        ]
    }
]

@app.route('/store', METHODS=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>/item')
def get_store(name):
    pass


@app.route('/store/')
def get_stores():
    pass


app.run(port=5000)
