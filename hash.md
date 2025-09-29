# Hashing Algorithm

Hashing algorithms are **one-way functions**, meaning they cannot be reversed to retrieve the original input data — and that's exactly their purpose. Hashing secures data at rest, ensuring that even if someone gains access to your server, the stored information remains unreadable.

![Hashing Algorithm Img](/docs/img/HashingAlgorithm.svg "Hashing Algorithm")

## Data integrity verification
Data integrity verification is the process of ensuring that data has not been altered, corrupted, or tampered with during storage or transmission. One of the most effective ways to verify data integrity is by using hash functions.
![File Validation Process Img](/docs/img/FileValidation.svg "File Validation")

### Validation file using Windows PowerShell
You can easily hash a file in **Windows PowerShell** using the built-in **`Get-FileHash`** cmdlet. Here’s how:

**SYNTAX:**
```PowerShell
Get-FileHash [-Path] <string[]> [-Algorithm {SHA1 | SHA256 | SHA384 | SHA512 | MACTripleDES | MD5 | RIPEMD160}]
```
**Example:**
> [!NOTE]
> On blender official website they will provide window installation file and list of checksum file (MD5, SHA256), we will used **MD5** for this example.

This is list of MD5 Check that got from blender official website:
```TXT
# blender-4.5.2.md5
16a313d4b66d4aa61a26da321fa78472  blender-4.5.2-macos-arm64.dmg
4068ec12cf84e54bde1951ee6dafdc84  blender-4.5.2-macos-x64.dmg
1c40c1edd6c406d63ccf04a872a68b0d  blender-4.5.2-linux-x64.tar.xz
aec3ee9723bf629399b34426321ccd6d  blender-4.5.2-windows-x64.msi
e2399dfd30428cb4bbe49a13e6bb797d  blender-4.5.2-windows-x64.msix
0dfe0df817e48ea4a4239f7a36013c38  blender-4.5.2-windows-x64.zip
992fa86d63aec18c112dc6eeff400efa  blender-4.5.2-windows-arm64.msi
d15ae42b07c69c993bbdd1b71cfebbd1  blender-4.5.2-windows-arm64.msix
0004137ce099727585da603672c195b4  blender-4.5.2-windows-arm64.zip
```
Run this command and compare hash to the checksum file:
```PowerShell
Get-FileHash -Path .\blender-4.5.2-windows-x64.msi -Algorithm MD5
```
**Output:**
```PowerShell
Algorithm       Hash                                  Path
---------       ----                                  ----
MD5             AEC3EE9723BF629399B34426321CCD6D      C:\Users\soth.pisey\Downloads\blender-4.5.2-windows...
```



Now Both hases look identical that's means the blender installation file is not corrupted and we could not install into the your computer safely.

## Password Storage
Instead of storing passwords in plain text, systems store their hash values. When you try to log in, the system hashes your entered password and compares it to the stored hash. This way, even if a database is compromised, the actual passwords are not directly revealed.

| id  | username  | password (SHA-256 hash)                                          | created_at          |
| --- | --------- | ---------------------------------------------------------------- | ------------------- |
| 1   | sothpisey | 3bc51062973c458d5de0ea5bbb7e0222cd1c90cbaec2022a253f8e2e4d8f2f84 | 2024-05-01 10:15:00 |
| 2   | bob       | bcb7a9b74d5aaeb5e19a31e4b2e92c04e26ff3b8355cf8d9ef07487ff8f6983c | 2024-05-02 11:45:00 |
| 3   | charlie   | 1b6453892473a467d07372d45eb05abc2031647a8cd7f5b48e0e6e051c2f8ecf | 2024-05-03 09:30:00 |

### User and Password hashed authentication process:

![Hashing Algorithm Img](/docs/img/password_hash_authentication.svg "Hashing Algorithm")

## Cracking Hash using Hashcat

```PowerShell
hashcat -m 0 -a 3 hashed.txt ?a?a?a?a?a?a
```

## JWT Token

Token: **<span style="color: green;">eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9</span>**.**<span style="color: cyan;">eyJpZCI6MTAsIm5hbWUiOiJzb3RocGlzZXkiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDY1OTM1ODF9</span>**.**<span style="color: yellow;">7ZvdZ4JpGRZS203UINHNl9istSEmucXO787AJOsS5a8</span>**


### Structure of JWT

![JWT structure diagram](/docs/img/jwt_structure.svg "JWT Structure")

### JWT Validation

![JWT validation diagram](/docs/img/jwt_validation.svg "JWT Validation")

