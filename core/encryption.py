import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


def derive_key(password: str, salt: bytes = b'st3g0n@gr@phy'):
    """Derives a cryptographic key from a user-provided password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_data(data, password):
    """Encrypts data using a password-derived key."""
    key = derive_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(data.encode()).decode()


def decrypt_data(encrypted_data, password):
    """Decrypts data using the same password-derived key."""
    key = derive_key(password)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data.encode()).decode()
