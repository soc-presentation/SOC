import hmac
import hashlib, base64

key = 'key'.encode()
message = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6InNvdGhwaXNleSIsImlhdCI6MTc0NjI5OTczN30'.encode()

hm = hmac.new(key, message, hashlib.sha256)

print(base64.b64encode(hm.digest()).decode())


# JWT token: 

# Signature: 