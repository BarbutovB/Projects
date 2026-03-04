def xor_cipher(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

secret_data = "BOZHIDAR BARBUTOV - LAW & CYBERSECURITY"
secret_key = 123

encrypted = xor_cipher(secret_data, secret_key)
print(f"{encrypted}")

decrypted = xor_cipher(encrypted, secret_key)
print(f"{decrypted}")
