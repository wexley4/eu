import psutil
import time

limite = float(input("Limite de RAM (%): "))

try:
    while True:
        mem = psutil.virtual_memory()
        print(f"Uso RAM: {mem.percent}%")
        if mem.percent > limite:
            print("⚠ ALERTA: RAM acima do limite!")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nEncerrado.")