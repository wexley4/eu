frase = input("Digite uma frase: ").lower()

cont = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for ch in frase:
    if ch in cont:
        cont[ch] += 1

print("Total de vogais:", sum(cont.values()))
print("Detalhado:", cont)