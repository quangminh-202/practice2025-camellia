import os
import random
import warnings
from camellia_modes import encrypt_camellia, decrypt_camellia
from error_simulation import corrupt_ciphertext
from analysis import plot_damage, plot_all_modes

warnings.filterwarnings("ignore", category=UserWarning)

BLOCK_SIZE = 16
MODES = ["ECB", "CBC", "CFB", "OFB"]
key = os.urandom(16)
iv = os.urandom(16)

with open("data/plaintext.txt", "rb") as f:
    original = f.read()

damage_results = {}

for mode in MODES:
    damaged = []

    iv_to_use = iv if mode != "ECB" else None
    ciphertext = encrypt_camellia(mode, key, iv_to_use, original)

    with open(f"data/{mode}_ciphertext.bin", "wb") as cipher_file:
        cipher_file.write(ciphertext)

    total_blocks = len(ciphertext) // BLOCK_SIZE
    max_n = min(total_blocks, 30)

    for n in range(1, max_n + 1):
        corrupted_blocks = random.sample(range(total_blocks), n)
        byte_indices = [random.randint(0, BLOCK_SIZE - 1) for _ in corrupted_blocks]

        corrupted = corrupt_ciphertext(ciphertext, BLOCK_SIZE, mode, corrupted_blocks, byte_indices)

        try:
            decrypted = decrypt_camellia(mode, key, iv_to_use, corrupted)
        except Exception:
            decrypted = b""

        m = 0
        min_len = min(len(original), len(decrypted))
        for i in range(0, min_len, BLOCK_SIZE):
            block_orig = original[i:i + BLOCK_SIZE]
            block_decrypt = decrypted[i:i + BLOCK_SIZE]
            if block_orig != block_decrypt:
                m += 1

        damaged.append(m)

    damage_results[mode] = damaged
    plot_damage(mode, damaged, list(range(1, len(damaged) + 1)))

plot_all_modes(damage_results)
