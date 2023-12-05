from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import base64


class KeyFormat(bytes):
    def format(self, format_type: str) -> str:
        ALLOWED_VALUES = ["base64", "string", "multiline"]
        if format_type not in ALLOWED_VALUES:
            raise ValueError(f"Invalid format. Allowed values are {ALLOWED_VALUES}")
        if format_type == "base64":
            return base64.b64encode(self).decode("utf-8")
        elif format_type == "string":
            key_text = self.decode('utf-8').splitlines()
            key_text = key_text[1:-1]
            key_text = ''.join(key_text)
            return key_text
        elif format_type == "multiline":
            return self.decode("utf-8")


class KeyPair:
    def __init__(self):                
        # Generate an RSA key pair
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Serialize the private key in PKCS#8 format
        self.private = KeyFormat(self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

        # Serialize the public key in PKCS#8 format
        self.public = KeyFormat(self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))


