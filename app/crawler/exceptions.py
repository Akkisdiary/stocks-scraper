class InvalidUrlException(Exception):
    def __init__(self, msg="Invalid url") -> "InvalidUrlException":
        super().__init__()
        self.message = msg


class UrlNotFoundException(Exception):
    def __init__(self, msg="Resource not found") -> "UrlNotFoundException":
        super().__init__()
        self.message = msg
