import psutil
import platform

print("Modelo/Identificação:", platform.processor() or "Não disponível")
print("Núcleos físicos:", psutil.cpu_count(logical=False))
print("Núcleos lógicos:", psutil.cpu_count(logical=True))

freq = psutil.cpu_freq()
if freq:
    print(f"Frequência atual: {freq.current:.0f} MHz | min: {freq.min:.0f} | max: {freq.max:.0f}")
else:
    print("Frequência: não disponível")

print("\nNúmero de série da CPU:")
print("Em geral não é acessível de forma portátil por segurança/permissões do sistema.")