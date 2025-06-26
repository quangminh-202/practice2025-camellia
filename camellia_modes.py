from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

BLOCK_SIZE = 16

def pad(data: bytes) -> bytes:
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len

def unpad(data: bytes) -> bytes:
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_camellia(mode_name, key, iv, plaintext):
    algo = algorithms.Camellia(key)
    mode = {
        "ECB": modes.ECB(),
        "CBC": modes.CBC(iv),
        "CFB": modes.CFB(iv),
        "OFB": modes.OFB(iv)
    }[mode_name]

    cipher = Cipher(algo, mode, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(pad(plaintext)) + encryptor.finalize()

def decrypt_camellia(mode_name, key, iv, ciphertext):
    algo = algorithms.Camellia(key)
    mode = {
        "ECB": modes.ECB(),
        "CBC": modes.CBC(iv),
        "CFB": modes.CFB(iv),
        "OFB": modes.OFB(iv)
    }[mode_name]

    cipher = Cipher(algo, mode, backend=default_backend())
    decryptor = cipher.decryptor()
    return unpad(decryptor.update(ciphertext) + decryptor.finalize())
