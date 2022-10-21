from flask import Flask, request
import base64


app = Flask(__name__)
data = ''

@app.route("/", methods=['GET'])
def index():
	return data

@app.route("/update_data", methods=['POST'])
def update_data():
	global data
	data = base64.b64decode(request.data)
	return {'status': 200}


if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		port=3000
	)

