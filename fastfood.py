from flask import Flask, jsonify

app = Flask(__name__)


app.config['SECRET_KEY'] = "philipotieno"

@app.route('/api/v1/', methods=['GET'])
def home():
	return jsonify({'message' : 'welcome to Fast-Food-Fast'}), 200



#Initalization
if __name__=="__main__":
	app.run(debug = True)
