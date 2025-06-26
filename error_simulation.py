import random
import copy

def corrupt_ciphertext(ciphertext: bytes, block_size: int, num_blocks: int) -> bytes:
    corrupted = bytearray(ciphertext)
    total_blocks = len(ciphertext) // block_size
    blocks_to_corrupt = random.sample(range(total_blocks), num_blocks)
    for block_idx in blocks_to_corrupt:
        byte_index = block_idx * block_size + random.randint(0, block_size - 1)
        corrupted[byte_index] ^= 0xFF  # lật bit
    return bytes(corrupted)
