from flask import Flask

application = app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World! This is a Flask app in a docker container."

@app.route('/route2')
def route2():
    return "This is route 2."

@app.route('/route2/<string:name>')
def get_name(name):
    return name

if __name__ == "__main__":
    app.run(debug = True, port = 5000)