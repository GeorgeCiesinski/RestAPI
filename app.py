from flask import Flask

# Normally Flask applications are called app.py

app = Flask(__name__)

stores = [
	{
		'name': 'My Wonderful Store',
		'items': [
			{
				'name': 'Product 1',
				'price': 29.99
			}
		]
	},
	{
		'name': 'My Other Store',
		'items': [
			{
				'name': 'Cool Product',
				'price': 45.99
			}
		]
	}
]


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
	pass


# GET /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/somename'
def get_store(name):
	pass


# GET /store
@app.route('/store')
def get_stores():
	pass


# POST /store/<string:name>/item { name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	pass

# Tell app to run, with a certain port
app.run(port=5000)
