import platform
import psutil
import wmi
import time

def get_cpu_temperature_unix():
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            return int(temps['coretemp'][0].current)
        else:
            print("Не удалось найти данные о температуре процессора.")
            return None
    except (AttributeError, KeyError, psutil.NoSuchProcess, psutil.AccessDenied):
        print("Ошибка при получении данных о температуре процессора.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при получении температуры: {e}")
        return None

def get_cpu_temperature_windows():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        sensors = w.Sensor()
        for sensor in sensors:
            if sensor.SensorType == "Temperature" and "CPU Core" in sensor.Name:
                return int(sensor.Value)
        print("Не удалось найти данные о температуре процессора.")
        return None
    except Exception as e:
        print(f"Ошибка при получении данных о температуре процессора: {e}")
        return None

def get_cpu_temperature():
    if platform.system() == "Windows":
        return get_cpu_temperature_windows()
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        return get_cpu_temperature_unix()
    else:
        print("Система не распознана.")
        return None

def main():
    filename = "cpu_temperatures.txt"
    try:
        with open(filename, 'w') as f:
            for _ in range(100):
                temp = get_cpu_temperature()
                if temp is not None:
                    print(f"Температура процессора: {temp} °C")
                    f.write(f"{temp}\n")
                else:
                    print("Не удалось измерить температуру процессора.")
                time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nИзмерение прервано.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")

if __name__ == "__main__":
    main()
