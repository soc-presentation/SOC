import json, base64, hmac, hashlib, time

def base64url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('ascii')

def encode_jwt(header, payload, secret):
    header_json = json.dumps(header, separators=(',', ':')).encode('utf-8')
    payload_json = json.dumps(payload, separators=(',', ':')).encode('utf-8')

    header_b64 = base64url_encode(header_json)
    payload_b64 = base64url_encode(payload_json)

    message = f'{header_b64}.{payload_b64}'.encode('utf-8')
    signature = hmac.new(secret.encode('utf-8'), message, hashlib.sha256).digest()
    signature_b64 = base64url_encode(signature)

    return f'{header_b64}.{payload_b64}.{signature_b64}'

if __name__ == '__main__':
    secret = 'soc'

    header = {
        "alg": "HS256",
        "typ": "JWT"
    }

    payload = {
        "id": 10,
        "name": "sothpisey",
        "role": "admin",
        "iat": int(time.time()), 
        "exp": 'none'
    }

    jwt_token = encode_jwt(header, payload, secret)
    print("JWT:", jwt_token)
