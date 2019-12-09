import os
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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)