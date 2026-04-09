import psutil
import time
import os

try:
    while True:
        os.system("cls")  # Windows

        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1)
        disk = psutil.disk_usage("C:\\")

        n1 = psutil.net_io_counters()
        time.sleep(1)
        n2 = psutil.net_io_counters()
        down = (n2.bytes_recv - n1.bytes_recv) / 1024
        up = (n2.bytes_sent - n1.bytes_sent) / 1024

        print("=== Painel ===")
        print(f"RAM: {mem.percent}% | Usado: {mem.used/1024**2:.0f} MB")
        print(f"CPU: {cpu}%")
        print(f"Disco (C:): Livre: {disk.free/1024**3:.2f} GB")
        print(f"Download: {down:.2f} kB/s | Upload: {up:.2f} kB/s")

        time.sleep(1)  # total ~2s por ciclo
except KeyboardInterrupt:
    print("\nEncerrado.")