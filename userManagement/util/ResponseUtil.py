class ResponseEntity:

    def __init__(self, status=200, body=None):
        self.status = status
        self.body = body

