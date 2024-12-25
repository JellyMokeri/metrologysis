import matplotlib.pyplot as plt
import re
import numpy as np

def plot_cpu_temperature_histogram(filename="cpu_temperatures.txt"):

    try:
        with open(filename, 'r') as f:
            temps = [int(line.strip()) for line in f if re.match(r"^\d+$", line.strip())]

        if not temps:
            print("Файл пуст или не содержит корректные числовые данные.")
            return

        min_temp = min(temps)
        max_temp = max(temps)

        bins = np.arange(min_temp, max_temp + 2, 1)

        plt.hist(temps, bins=bins, edgecolor='black')
        plt.xlabel("Температура (°C)")
        plt.ylabel("Количество измерений")
        plt.title("Гистограмма температур процессора")
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError as e:
        print(f"Ошибка при чтении данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    plot_cpu_temperature_histogram()
