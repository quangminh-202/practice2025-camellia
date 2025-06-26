import matplotlib.pyplot as plt
import os

def plot_damage(mode_name, damaged_blocks, N_values):
    os.makedirs("results", exist_ok=True)
    plt.plot(N_values, damaged_blocks, marker='o')
    plt.xlabel("Number of corrupted blocks in ciphertext (N)")
    plt.ylabel("Number of corrupted blocks in plaintext (M)")
    plt.title(f"Error propagation in {mode_name} mode")
    plt.grid(True)
    plt.savefig(f"results/{mode_name}_damage.png")
    plt.clf()
