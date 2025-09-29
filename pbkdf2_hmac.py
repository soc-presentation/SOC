import hashlib, secrets, base64, random

def get_password(password: str) -> str:
    iterations = random.randint(200000, 300000)
    
    salt = secrets.token_hex(6)
    
    dk = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        iterations
    )
    
    hash_b64 = base64.b64encode(dk).decode().strip()
    
    return f"{iterations}${salt}${hash_b64}"

if __name__ == "__main__":
    print(get_password("super_secret"))
