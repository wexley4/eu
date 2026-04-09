import psutil

limite_livre = 10  # % livre mínimo

print(f"Partições críticas (livre < {limite_livre}%):")
for part in psutil.disk_partitions():
    try:
        uso = psutil.disk_usage(part.mountpoint)
        livre_pct = 100 - uso.percent
        if livre_pct < limite_livre:
            print(f"⚠ {part.mountpoint} | Livre: {livre_pct:.1f}%")
    except PermissionError:
        continue