import hashlib

input = 'snail'

hashed_text = hashlib.md5(input.encode())

print(f'{hashed_text.hexdigest().upper()} : {input}')