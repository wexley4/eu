import psutil

try:
    while True:
        por_nucleo = psutil.cpu_percent(interval=1, percpu=True)
        total = sum(por_nucleo) / len(por_nucleo)
        print(f"CPU Total: {total:.1f}%")
        print(" | ".join([f"Núcleo {i}: {v:.1f}%" for i, v in enumerate(por_nucleo)]))
        print("-" * 50)
except KeyboardInterrupt:
    print("\nEncerrado.")