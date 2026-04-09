import psutil
import time
from datetime import datetime

ARQ = "cpu_log.txt"

try:
    while True:
        uso = psutil.cpu_percent(interval=1)
        with open(ARQ, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - CPU: {uso:.1f}%\n")
        time.sleep(4)  # +1 do interval = ~5s total
except KeyboardInterrupt:
    print("\nEncerrado.")