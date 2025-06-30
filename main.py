import os
from camellia_modes import encrypt_camellia, decrypt_camellia
from error_simulation import corrupt_ciphertext
from analysis import plot_damage

BLOCK_SIZE = 16
MODES = ["ECB", "CBC", "CFB", "OFB"]
key = os.urandom(16)
iv = os.urandom(16)

with open("data/plaintext.txt", "rb") as f:
    original = f.read()

for mode in MODES:
    damaged = []
    ciphertext = encrypt_camellia(mode, key, iv, original)

    with open(f"data/{mode}_ciphertext.bin", "wb") as cipher_file:
        cipher_file.write(ciphertext)

    for n in range(1, 11):
        corrupted = corrupt_ciphertext(ciphertext, BLOCK_SIZE, n)

        with open(f"data/{mode}_corrupted_{n}.bin", "wb") as corrupt_file:
            corrupt_file.write(corrupted)
        try:
            decrypted = decrypt_camellia(mode, key, iv, corrupted)
        except Exception:   
            decrypted = b""

        m = sum(
            1 for i in range(0, len(original), BLOCK_SIZE)
            if original[i:i+BLOCK_SIZE] != decrypted[i:i+BLOCK_SIZE]
        )
        damaged.append(m)

        print(f"Mode: {mode}, N (corrupted blocks): {n}, M (damaged blocks in plaintext): {m}")

    plot_damage(mode, damaged, list(range(1, 11)))
