# Web Server From Scratch

A simple HTTP web server built from scratch using Python sockets.

This project was created to understand how web servers and frameworks work internally by implementing HTTP request handling manually without using **Flask**, **FastAPI**, **Django**, or any other web framework.

## Features

* TCP socket server
* HTTP/1.1 response handling
* GET request support
* POST request support
* Basic routing
* HTTP request parsing
* Custom response generation
* No external dependencies

## Project Structure

```
.
├── server.py
├── verbose.py
└── README.md
```

## Files

### server.py

Handles:

* Socket creation
* Server binding
* Listening for connections
* Accepting client requests
* HTTP request parsing
* Route matching
* Response generation
* Sending HTTP responses

### verbose.py

Contains helper functions for creating HTTP responses.

## How It Works

### 1. Create a TCP Socket

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Creates a TCP socket that allows the server to communicate with clients.

---

### 2. Bind to a Port

```python
server.bind(("localhost", 8080))
```

Assigns the server to a specific address and port.

---

### 3. Listen for Connections

```python
server.listen()
```

Waits for incoming client connections.

---

### 4. Accept Requests

```python
client, addr = server.accept()
```

Accepts a client connection and starts processing the request.

---

### 5. Parse HTTP Requests

Example request:

```
GET /about HTTP/1.1
Host: localhost:8080
```

The server extracts:

* HTTP Method
* Route Path
* Request Headers
* Request Body

---

### 6. Generate HTTP Responses

Example response:

```
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World</h1>
```

The server manually builds and sends HTTP responses.

# Routes

## GET /

Returns:

```html
<h1>Home Page</h1>
```

---

## GET /about

Returns:

```html
<h1>About Page</h1>
```

---

## POST /login

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

# Running The Server

Clone the repository:

```bash
git clone <repository-url>
```

Run:

```bash
python server.py
```

Open:

```
http://localhost:8080
```

# Example Requests

## GET Request

```bash
curl http://localhost:8080
```

## POST Request

```bash
curl -X POST \
-d "username=test&password=123" \
http://localhost:8080/login
```

# Learning Goals

This project demonstrates:

* TCP networking fundamentals
* Socket programming
* HTTP protocol basics
* Request/response lifecycle
* Routing systems
* How web frameworks work internally

# Future Improvements

Planned improvements:

## Planned Improvements

The goal of this project is to gradually evolve this basic HTTP server into a lightweight web framework by adding features commonly found in modern backend frameworks.

### Core Architecture

* Improve request handling with a dedicated `Request` object
* Add a `Response` object for managing:

  * Status codes
  * Headers
  * Cookies
  * Content types
* Create a cleaner server lifecycle and component-based architecture

### Routing System

* Dynamic route parameters

Example:

```
/users/<id>
/posts/<post_id>
```

* Route registration system
* Flask-like decorator-based routing

Example:

```python
@app.route("/")
def home():
    return "Hello World"
```

### Middleware System

Add support for request processing layers:

* Logging middleware
* Authentication middleware
* Rate limiting middleware
* Request validation

Example flow:

```
Request
   |
Middleware
   |
Router
   |
Controller
   |
Response
```

### Template Engine

Improve HTML rendering with:

* Template variables
* Dynamic HTML generation
* Template inheritance

Example:

```html
<h1>Hello {{ username }}</h1>
```

### Static File Handling

Support serving:

* CSS files
* JavaScript files
* Images
* Other assets

Example:

```
/static/style.css
/static/app.js
```

### Performance Improvements

* Multithreaded request handling
* Async I/O support
* Better connection management
* Improved request parsing

### Advanced Web Features

* Cookie handling
* Session management
* JSON API responses
* File uploads
* WebSocket support

### Final Goal

Transform the project from a basic socket-based HTTP server into a lightweight educational web framework that demonstrates how frameworks like Flask and Express work internally.


# License

MIT License
