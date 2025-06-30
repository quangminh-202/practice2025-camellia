import matplotlib.pyplot as plt
import os

COLOR_MAP = {
    "ECB": "red",
    "CBC": "blue",
    "CFB": "green",
    "OFB": "orange"
}

LINESTYLES = {
    "ECB": "-",
    "CBC": "--",
    "CFB": "-.",
    "OFB": ":"
}

MARKERS = {
    "ECB": "o",
    "CBC": "s",
    "CFB": "D",
    "OFB": "^"
}

def plot_damage(mode_name, damaged_blocks, N_values):
    os.makedirs("results", exist_ok=True)
    plt.figure(figsize=(10, 6))
    color = COLOR_MAP.get(mode_name, "black")
    linestyle = LINESTYLES.get(mode_name, "-")
    marker = MARKERS.get(mode_name, "o")
    plt.plot(N_values, damaged_blocks, marker=marker, linestyle=linestyle, color=color)
    plt.xlabel("Число повреждённых блоков шифртекста (N)")
    plt.ylabel("Число искажённых блоков открытого текста (M)")
    plt.title(f"Распространение ошибок в режиме {mode_name}")
    plt.grid(True)
    plt.savefig(f"results/{mode_name}_damage.png")
    plt.clf()

def plot_all_modes(damage_dict):
    os.makedirs("results", exist_ok=True)
    plt.figure(figsize=(12, 8))
    for mode_name, damaged_blocks in damage_dict.items():
        x_values = list(range(1, len(damaged_blocks) + 1))
        color = COLOR_MAP.get(mode_name, "black")
        linestyle = LINESTYLES.get(mode_name, "-")
        marker = MARKERS.get(mode_name, "o")
        plt.plot(x_values, damaged_blocks, marker=marker, linestyle=linestyle,
                 label=mode_name, color=color)

    plt.xlabel("Число повреждённых блоков шифртекста (N)")
    plt.ylabel("Число искажённых блоков открытого текста (M)")
    plt.title("Сравнение распространения ошибок в различных режимах")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/all_modes_damage.png")
    plt.clf()
