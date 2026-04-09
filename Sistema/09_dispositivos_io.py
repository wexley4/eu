import psutil

# Dispositivos de E/S (Entrada/Saída) incluem:
# - teclado, mouse (entrada)
# - monitor, impressora (saída)
# - disco/SSD/pendrive (entrada e saída)
# Aqui listamos partições de armazenamento (mais fácil via código).

parts = psutil.disk_partitions()
for i, p in enumerate(parts, 1):
    print(f"{i}) {p.device} -> {p.mountpoint}")

esc = int(input("Escolha um número da lista: "))
p = parts[esc - 1]

uso = psutil.disk_usage(p.mountpoint)
print("\nDetalhes:")
print("Device:", p.device)
print("Mount:", p.mountpoint)
print("Total:", uso.total / 1024**3, "GB")
print("Usado:", uso.used / 1024**3, "GB")
print("Livre:", uso.free / 1024**3, "GB")
print("Uso%:", uso.percent)