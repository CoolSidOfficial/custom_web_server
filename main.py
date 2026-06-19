import socket
from verabose import make_response, render_template
from rate_limiter import RateLimiter
class Request:
    def __init__(self, raw_request):

        self.raw = raw_request

        first_line = raw_request.split("\r\n")[0]

        self.method = first_line.split(" ")[0]
        self.path = first_line.split(" ")[1]

        parts = raw_request.split("\r\n\r\n")
        self.body = parts[1] if len(parts) > 1 else ""


class WebServer:

    def __init__(self, host="localhost", port=8080):

        self.host = host
        self.port = port
        self.rate_limiter = RateLimiter(
            limit=5,
            window=60
        )


        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

    def start(self):

        self.server.bind(
            (self.host, self.port)
        )

        self.server.listen()

        print(
            f"Server running on http://{self.host}:{self.port}"
        )

        while True:

            client, addr = self.server.accept()

            raw_request = client.recv(
                1024
            ).decode()

            if not raw_request:
                client.close()
                continue

            request = Request(raw_request)

            print(f"Method: {request.method}")
            print(f"Path: {request.path}")
            print(f"Body: {request.body}")
            print("-" * 50)

            response = self.handle_request(
                request
            )

            client.sendall(
                response.encode()
            )

            client.close()

    def handle_request(self, request):

        if (
            request.method == "GET"
            and request.path == "/"
        ):
            return make_response(
                render_template("index.html")
            )

        elif (
            request.method == "GET"
            and request.path == "/about"
        ):
            return make_response(
                render_template("about.html")
            )

        elif (
            request.method == "POST"
            and request.path == "/login"
        ):
            return make_response(
                f"""
                <h1>Login Received</h1>
                <p>{request.body}</p>
                """
            )

        return make_response(
            "<h1>404 Not Found</h1>"
        )


if __name__ == "__main__":

    app = WebServer()
    app.start()