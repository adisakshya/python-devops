from flask import Flask

application = app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World! This is a Flask application server 'A'."

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')