from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# response with JSON
@app.route("/user")
def get_user():
    return {
        'name': 'Example User',
        'age': 28
    }