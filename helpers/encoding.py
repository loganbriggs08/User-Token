import base64

class Encode:
    def string(string: str) -> str:
        base64_bytes = base64.b64encode(string.encode('utf-8'))
        
        if "=" in base64_bytes.decode('utf-8'):
            base64_bytes = base64_bytes.decode('utf-8').replace("=", "")
            return base64_bytes
        else:
            return base64_bytes