# Flask framework

## What is Flask?
- Python microframework for building web apps
- [Can do everything you need and nothing you don't](https://flask.palletsprojects.com/en/2.1.x/foreword/)
  Open source

## Why did we choose Flask?
- Lightweight
- It's designed to be easy to use and installed
- Might be "micro" but it has many functionalities
- It uses Jinja (you're already familiar with it)
- Independent (does not rely on any other external libraries to perform needed tasks)

# REST APIs

## And what are those, really?
- Going by the book: **RE**presentational **S**tate **T**ransfer architectural style used in modern web development which defines rules/constrains for a web application to send and receive data.
- In translation: architecture that uses HTTP protocol to access and use data.
- Key terms: client and resource
- When a RESTful API is called, the server transfers to the client a representation of the state of the requested resource

# Back to Flask

## Installation

Everytime you create a new project in Python, our reccomandation is to start by creating a virtual environment so you don't alter anything you already have installed on your local machine:

`python3 -m venv final-project-venv`
`source final-project-venv/bin/activate`

> **NOTE:** To deactivate a virtual environment, just write `deactivate` command in the terminal. To activate it, you need to use the second command from above.

Install required libraries: **Flask** and **flask-restful**:

`pip3 install flask`
`pip3 install flask-restful`

And Voilà! You can now start implementing your REST API using Flask.

## Usage

Let's see how exactly we use Flask and Python to write an API endpoint. You can do this in multiple ways.

### 1st approach: use only Flask

```
from flask import Flask, jsonify

demo = Flask(__name__)

@demo.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world'})

if __name__ == '__main__':
  demo.run(host="0.0.0.0", port=5002, debug=True)
```

- `from flask import Flask, jsonify`: Import the needed library;
- `demo = Flask(__name__)`: Create an instance of the Flask class;
- `@demo.route('/', methods=['GET'])`: `route()` decorator is used to tell Flask what URL will trigger our function and `methods` option is used to specify the HTTP method which triggers the function;
- `if __name__ == '__main__'`: `__name__` is a special variable in Python which takes the value of the script name. This line ensures that our Flask app runs only when it is executed in the main file and not when it is imported in some other file;
- `demo.run(host="0.0.0.0", port=5002, debug=True)`: Used to actually start the application. We also defined the host where we want our Flask app to run, the port and from a developer perspective, we activated the debug as well. The `0.0.0.0` means *all IPv4 addresses on the local machine*, the default for the *host* being `localhost` or `127.0.0.1`. The default value for *port* is `5000`, but in this case, we changed it for the sake of the demo.

Let's run the app!

`python3 demo-1.py`

You should see in the command line output something of the sorts:

```
  * Serving Flask app 'demo' (lazy loading)
  * Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
  * Debug mode: on
  * Running on all addresses (0.0.0.0)
  WARNING: This is a development server. Do not use it in a production deployment.
  * Running on http://127.0.0.1:5002
  * Running on http://172.17.1.167:5002 (Press CTRL+C to quit)
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: 396-627-189
```
You'll be able to see a lot of valuable information about the development server here. For more complex implementations and operations, if your code has bugs, you will receive an error in the browser or wherever you are testing the endpoints. Depending on the complexity, you will need to make use of the `Debugger PIN`.

Let's test now. You'll have to open a new command line prompt, as our Flask app is a forever-running-proccess.

`curl -v localhost:5002`

The output should look something like this:

```
  *   Trying 127.0.0.1:5002...
  * Connected to localhost (127.0.0.1) port 5002 (#0)
  > GET / HTTP/1.1
  > Host: localhost:5002
  > User-Agent: curl/7.79.1
  > Accept: */*
  >
  * Mark bundle as not supporting multiuse
  < HTTP/1.1 200 OK
  < Server: Werkzeug/2.1.2 Python/3.9.12
  < Date: Thu, 26 May 2022 09:01:56 GMT
  < Content-Type: text/html; charset=utf-8
  < Content-Length: 12
  < Connection: close
  <
  < Connection: close
  <
  {
    "message": "hello demo-1"
  }
  * Closing connection 0
```

As you can see, we have succesfully reached our application. This was a simple test done directly with `curl` in the command line as we defined this endpoint to respond on a `GET` method. When you are using more complex methods, like `POST` or `PUT`, we reccommend you use [Postman](https://www.postman.com/).

If you take a look at you Flask proccess, you will be able to see the request we made with a timestamp as well:

`127.0.0.1 - - [26/May/2022 12:01:56] "GET / HTTP/1.1" 200 -`

> **NOTE:** Keep an eye on the terminal where you have the Flask proccess, when you'll troubleshoot and want to use the holy `print("Why are you not working?")` you will see the print in there, not in the client you are using to test the code. Code exceptions will appear here as well.

### 2nd approace: use flask-restful

```
from flask import Flask, jsonify
from flask_restful import Resource, Api

demo = Flask(__name__)
api = Api(demo)

class Hello(Resource):
	def get(self):
		return jsonify({'message': 'hello demo-2'})

api.add_resource(Hello, '/')

if __name__ == '__main__':
	demo.run(host="0.0.0.0", port=5003, debug=True)
```

- `from flask import Flask, jsonify` and `from flask_restful import Resource, Api`: Import the needed libraries, observe that this time we added some classes from the `flask_restful` library;
- `demo = Flask(__name__)`: Create an instance of the Flask class;
- `api = Api(demo)`: Create an API object;
- `class Hello(Resource):`: Create a class for a particular `Resource`. The get, post methods correspond to `GET` and `POST` requests and they are automatically mapped by `flask_restful`;
- `def get(self):`: corresponds to the `GET` request. This function is called whenever there is a `GET` request for this resource;
- `api.add_resource(Hello, '/')`: Adding the defined resources along with their corresponding URLs.

This code behaves the exact same way as the one from the 1st approach so you will have the same output.

When you write the code for your project you can use either approach or mix and match them. We ancourage you to discover more by browsing the Flask documentation:
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/)