import random


def app(environ, start_response):
    data = b"Test Server\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length"), str(len(data))
    ])

    if random.choice([True, False]):
        breakpoint()

    return iter([data])