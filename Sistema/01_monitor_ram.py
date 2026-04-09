import psutil
import time

while True:
    mem = psutil.virtual_memory()
    total = mem.total / 1024**2
    usado = mem.used / 1024**2
    livre = mem.available / 1024**2

    print(f"Total: {total:.2f} MB | Usado: {usado:.2f} MB | Livre: {livre:.2f} MB | Uso: {mem.percent}%")
    time.sleep(2)