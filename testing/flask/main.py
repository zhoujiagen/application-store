from flask import Flask
import os

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

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=os.environ.get('APP_PORT', 5000))