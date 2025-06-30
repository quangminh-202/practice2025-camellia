from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

BLOCK_SIZE = 16

def pad(data: bytes) -> bytes:
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len

def unpad(data: bytes) -> bytes:
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_camellia(mode_name, key, iv, plaintext):
    algo = algorithms.Camellia(key)

    if mode_name == "ECB":
        mode = modes.ECB()
        padded_data = pad(plaintext)
    elif mode_name == "CBC":
        mode = modes.CBC(iv)
        padded_data = pad(plaintext)
    elif mode_name == "CFB":
        mode = modes.CFB(iv)
        padded_data = plaintext
    elif mode_name == "OFB":
        mode = modes.OFB(iv)
        padded_data = plaintext
    else:
        raise ValueError(f"Unsupported mode: {mode_name}")

    cipher = Cipher(algo, mode, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data) + encryptor.finalize()

def decrypt_camellia(mode_name, key, iv, ciphertext):
    algo = algorithms.Camellia(key)

    if mode_name == "ECB":
        mode = modes.ECB()
    elif mode_name == "CBC":
        mode = modes.CBC(iv)
    elif mode_name == "CFB":
        mode = modes.CFB(iv)
    elif mode_name == "OFB":
        mode = modes.OFB(iv)
    else:
        raise ValueError(f"Unsupported mode: {mode_name}")

    cipher = Cipher(algo, mode, backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    if mode_name in ["ECB", "CBC"]:
        return unpad(decrypted_data)
    else:
        return decrypted_data
