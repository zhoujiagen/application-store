# Flask

Functioning as a REST endpoint for testing.

- https://flask.palletsprojects.com/

Setup and run:

```shell
# Windows using Git Bash
$ python --version
Python 3.11.5
$ python -m virtualenv .venv

$ source .venv/Scripts/activate
$ .venv/Scripts/pip install Flask
$ .venv/Scripts/pip freeze > requirements.txt

$ .venv/Scripts/flask --app hello routes
Endpoint     Methods  Rule
-----------  -------  -----------------------
hello_world  GET      /
static       GET      /static/<path:filename>

# for hello.py
$ .venv/Scripts/flask --app hello run --port 5000 --debug
 * Serving Flask app 'hello'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 753-664-915
127.0.0.1 - - [12/Mar/2024 09:38:19] "GET / HTTP/1.1" 200 -

$ curl http://127.0.0.1:5000
<p>Hello, World!</p>
$ curl http://127.0.0.1:5000/user -H "Accept: application/json"
{
  "age": 28,
  "name": "Example User"
}
```