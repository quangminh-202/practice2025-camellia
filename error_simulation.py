import random

def corrupt_ciphertext(ciphertext: bytes, block_size: int, mode_name: str,
                       corrupted_blocks: list[int], byte_indices: list[int]) -> bytes:
    corrupted = bytearray(ciphertext)

    for block_idx, byte_in_block in zip(corrupted_blocks, byte_indices):
        start = block_idx * block_size

        if mode_name in ["ECB", "CBC"]:
            for i in range(block_size):
                corrupted[start + i] ^= 0xFF
        else:
            corrupted[start + byte_in_block] ^= 0xFF

    return bytes(corrupted)
