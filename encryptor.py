def xor_encrypt_decrypt(text, key):
    """Encrypt or decrypt a string using XOR with a single-byte key."""
    return ''.join(chr(ord(char) ^ key) for char in text)

encrypted = xor_encrypt_decrypt('Library AI Elaine Rich Kevin Knight, Shivashankar B Nair: Artificial Intelligence, Tata McGraw Hill 3rd edition 2013.', 35)
print("Encrypted:", [ord(encrypted[i]) for i in range(len(encrypted))])

def encrypt_path(path, key=35):
    encrypted_path = []
    for x, y in path:
        encrypted_x = x ^ key
        encrypted_y = y ^ key
        encrypted_path.append((encrypted_x, encrypted_y))
    return encrypted_path

clue_path = [
    (0, 1),  # K
    (0, 2),  # A
    (3, 5),  # 2
    (3, 5),  # 2
    (2, 1),  # E
    (4, 0),  # G
    (2, 3),  # 0
    (0, 5),  # 5
    (5, 5),  # 6
    (5, 0)   # 7
]

encrypted_path = encrypt_path(clue_path, 35)
print("Encrypted Clue Path:", encrypted_path)