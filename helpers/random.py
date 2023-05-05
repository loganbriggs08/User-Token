import string
import secrets

class Random:
    def string() -> str:
        return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(25))