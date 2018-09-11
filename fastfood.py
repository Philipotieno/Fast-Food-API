from flask import Flask, jsonify

app = Flask(__name__)


app.config['SECRET_KEY'] = "philipotieno"

@app.route('/api/v1/', methods=['GET'])
def home():
	return jsonify({'message' : 'welcome to Fast-Food-Fast'}), 200

#Register new user
@app.route('/api/v1/register', methods=['POST'])
def register():
	name = request.get_json()['name']
	username = request.get_json()['username']
	email = request.get_json()['email']
	password = request.get_json()['password']

	if username not in user:
		user.update({username:{"name":name, "email":email, "password":password}})
		return jsonify(user), 200

	else:
		return jsonify({"message" : "User already registered"})

#Login authorisation
def log_auth(username, password):
	if username in user:
		if password == user[username]['password']:
			return True
	return False

#check if user is in session
def check_user(func):
	@wraps(func)
	def wrap(*args, **kwargs):
		if session["check_user"]:
			return func(*args, **kwargs)
		else:
			return jsonify({'message' : "please login to continue"}), 401

	return wrap
	
#Login if registered
@app.route('/api/v1/login', methods=['POST'])
def login():
	username = request.get_json()['username']
	password = request.get_json()['password']
	if log_auth(username,password):
		session['check_user'] = True
		session['username'] = username
		return jsonify({'message' : 'welcome to Fast-Food-Fast'}), 200
	else:
		return jsonify({'message' : "invalid details"}), 401

#Initalization
if __name__=="__main__":
	app.run(debug = True)
