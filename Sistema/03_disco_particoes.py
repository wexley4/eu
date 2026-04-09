import psutil

def gb(x): return x / 1024**3

print(f"{'Montagem':<20} {'Total(GB)':>10} {'Usado(GB)':>10} {'Livre(GB)':>10} {'Uso%':>6}")
print("-" * 62)

for part in psutil.disk_partitions():
    try:
        uso = psutil.disk_usage(part.mountpoint)
        print(f"{part.mountpoint:<20} {gb(uso.total):>10.2f} {gb(uso.used):>10.2f} {gb(uso.free):>10.2f} {uso.percent:>6.1f}")
    except PermissionError:
        continue