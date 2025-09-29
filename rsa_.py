import rsa, base64

(public_key, private_key) = rsa.newkeys(512)

print(public_key)
print(private_key)