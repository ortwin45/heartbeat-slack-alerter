from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/heartbeat/<customer>/<site>/<id>')
def heartbeat(customer: str, site: str, id: str):
	return f'Hello {customer}, {site}, {id}'


