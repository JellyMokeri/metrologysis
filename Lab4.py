import numpy as np

def analyze_cpu_temperatures(filename="cpu_temperatures.txt"):

    try:
        with open(filename, 'r') as file:
            temps = [int(line.strip()) for line in file if line.strip().isdigit()]

        if not temps:
            print("Файл пуст или не содержит корректных числовых данных.")
            return None

        temps_array = np.array(temps)
        mean = np.mean(temps_array)
        std_dev = np.std(temps_array)
        return mean, std_dev

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None
    except ValueError as e:
        print(f"Ошибка при чтении данных: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

if __name__ == "__main__":
    mean, std_dev = analyze_cpu_temperatures()
    if mean is not None:
        print(f"Математическое ожидание: {mean:.1f} °C")
        print(f"Среднеквадратическое отклонение: {std_dev:.4f} °C")
