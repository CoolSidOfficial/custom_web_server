def make_response(body):
    return (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "\r\n"
        f"{body}"
    )
def render_template(filename):
    with open(f"templates/{filename}", "r") as f:
        return f.read()