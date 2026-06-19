                            )
n Web Server From Scratch

A simple HTTP web server built from scratch using Python sockets.

This project was created to understand how web servers and frameworks work under the hood by implementing HTTP request handling manually without using Flask, FastAPI, Django, or any other web framework.

## Features

* TCP socket server
* HTTP/1.1 response handling
* GET request support
* POST request support
* Basic routing
* Request parsing
* Custom response generation
* No external dependencies

## Project Structure

```text
.
├── server.py
├── verbose.py
└── README.md
```

### server.py

Handles:

* Socket creation
* Listening for connections
* Request parsing
* Route matching
* Response sending

### verbose.py

Contains helper functions for creating HTTP responses.

## How It Works

### 1. Create a TCP Socket

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### 2. Bind to a Port

```python
server.bind(("localhost", 8080))
```

### 3. Listen for Connections

```python
server.listen()
```

### 4. Accept Requests

```python
client, addr = server.accept()
```

### 5. Parse HTTP Requests

Example request:

```http
GET /about HTTP/1.1
Host: localhost:8080
```

The server extracts:

* HTTP Method
* Route Path
* Request Body

### 6. Generate HTTP Responses

Example response:

```http
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World</h1>
```

## Routes

### GET /

Returns:

```html
<h1>Home Page</h1>
```

### GET /about

Returns:

```html
<h1>About Page</h1>
```

### POST /login

Accepts form data and returns the received payload.

Example:

```bash
curl -X POST \
-d "username=sid&password=123" \
http://localhost:8080/login
```

Response:

```html
<h1>Login Received</h1>
```

## Running the Server

```bash
python server.py
```

Open:

```text
http://localhost:8080
```

## Example Requests

### GET Request

```bash
curl http://localhost:8080
```

### POST Request

```bash
curl -X POST \
-d "username=test&password=123" \
http://localhost:8080/login
```

## Learning Goals

This project demonstrates:

* TCP networking fundamentals
* Socket programming
* HTTP protocol basics
* Request/response lifecycle
* Route handling
* Foundation of web frameworks

## Future Improvements

* Request object abstraction
* Response object abstraction
* Dynamic route parameters
* Middleware support
* Template rendering
* Static file serving
* Multithreading
* Async I/O
* Flask-like decorators
* Mini web framework architecture

## License

MIT



