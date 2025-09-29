import base64

def base64url_decode(data):
    padding = '=' * ((4 - len(data) % 4) % 4)
    return base64.urlsafe_b64decode(data + padding)

payload = 'eyJpZCI6MTAsIm5hbWUiOiJzb3RocGlzZXkiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDYzMDE0MjQsImV4cCI6Im5vbmUifQ'
decoded = base64url_decode(payload).decode()

print(decoded)
