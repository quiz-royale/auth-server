class NoSuchUserException(Exception):
    def __init__(self) -> None:
        self.message = 'Invalid username or password!'
        super().__init__(self.message)
