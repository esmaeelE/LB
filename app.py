from  flask  import  Flask, jsonify
app = Flask(__name__)

from flask import request

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
        return jsonify({'ip': request.remote_addr}), 200

@app.route('/')
def  hello_world():
	response = {'message': 'Hello, World!'}
	return  jsonify(response)

if  __name__ =='__main__':
	app.run(host='0.0.0.0', port=5000) 
	# app.run(host='127.0.0.1', port=5000) 

# add Flask==2.2.2 & Werkzeug==2.2.2 in requirements.txt


