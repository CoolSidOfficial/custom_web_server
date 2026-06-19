import time


class RateLimiter:

    def __init__(self, limit=5, window=60):
        self.limit = limit
        self.window = window
        self.requests = {}


    def allow(self, client_ip):

        now = time.time()

        if client_ip not in self.requests:
            self.requests[client_ip] = []


        
        self.requests[client_ip] = [
            request_time
            for request_time in self.requests[client_ip]
            if now - request_time < self.window
        ]


        
        if len(self.requests[client_ip]) >= self.limit:
            return False


        self.requests[client_ip].append(now)

        return True