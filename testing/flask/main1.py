from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World - {sys.argv[2]}!</p>"

# response with JSON
@app.route("/user")
def get_user():
    return {
        'name': f'Example User - {sys.argv[2]}',
        'age': 28
    }

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))