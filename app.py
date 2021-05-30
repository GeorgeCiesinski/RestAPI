from flask import Flask, jsonify, request, render_template

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
	}
]


# This endpoint renders html template.
@app.route('/')
def home():
	"""
	Flask APIs should not render templates unless you are making a flask web app
	"""

	return render_template('index.html')


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():

	# Gets request sent by client. get_json() parses the json data and returns it
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)

	return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/somename'
def get_store(name):

	# Iterate over stores
	for store in stores:
		# Return store if found
		if store['name'] == name:
			return jsonify(store)
	# Return error if not
	return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})


# POST /store/<string:name>/item { name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):

	# Parse json data and extract it
	request_data = request.get_json()

	# Find store with matching name
	for store in stores:
		if store['name'] == name:
			# Create new item
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			# Append item to item list
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):

	# Iterate over stores
	for store in stores:
		# Return store items in a dict if found
		if store['name'] == name:
			return jsonify({'items': store['items']})
	# Return error if not
	return jsonify({'message': 'store not found'})


# Tell app to run, with a certain port
app.run(port=5000)
