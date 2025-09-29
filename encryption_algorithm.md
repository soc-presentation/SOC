# Encryption Algorithm
An encryption algorithm is a set of rules (a mathematical process) that takes plaintext (normal readable data) and a key, and transforms it into ciphertext (scrambled unreadable data).
![Encryption Algorithm Img](/docs/img/EncryptionAlgorithm.svg "Encryption Algorithm")

**There are two types of Encryption Algorithm:**

- Symmetric Encryption
- Asymmetric Encryption

![Symmetric vs Asymmetric algorithm Img](/docs/img/Symmetric-vs-Asymmetric.png "Symmetric vs Asymmetric algorithm")

## Symmetric Encryption
Symmetric encryption uses a single secret key to both encrypt (scramble) and decrypt (unscramble) data, ensuring confidentiality for authorized parties. It is a fast and efficient method for securing large volumes of data but requires a secure way to exchange the shared key between the sender and recipient.

![Symmetric Encryption Img](/docs/img/SymmetricEncryption.png "Symmetric Encryption")

## Asymmetric Encryption
Asymmetric encryption, also referred to as **public key encryption**, employs two distinct keys: one for encryption, which is **public key**, and another for decryption, which is **private key (Secret Key)**. Entities may use this encryption to protect data and key exchanges over open, insecure channels. They also use it to authenticate and ensure data integrity.
![Asymmetric Encryption Img](/docs/img/AsymmetricEncryption.png "Asymmetric Encryption")

### RSA (Rivest–Shamir–Adleman)
Generate SSH Key pair using RSA algorithm:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Put it into remote server:
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server_ip_or_hostname
```

### ECC (Elliptic-Curve cryptography)