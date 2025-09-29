""" 
import hashlib, base64, secrets
import base64
import secrets

def pbkdf2_sha256_hash(password, salt=None, iterations=260000):
    if salt is None:
        salt = secrets.token_hex(16)  # 32 characters (16 bytes)
    
    password = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    
    dk = hashlib.pbkdf2_hmac('sha256', password, salt_bytes, iterations)
    hash_b64 = base64.b64encode(dk).decode('ascii').strip()

    return f'pbkdf2_sha256${iterations}${salt}${hash_b64}'

hashed = pbkdf2_sha256_hash('sothpisey')
print("Hashed:", hashed)
 """


