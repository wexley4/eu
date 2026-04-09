def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

while True:
    print("\n1) Somar  2) Subtrair  3) Multiplicar  4) Dividir  0) Sair")
    op = input("Escolha: ")

    if op == "0":
        break

    a = float(input("A: "))
    b = float(input("B: "))

    if op == "1":
        print("Resultado:", somar(a, b))
    elif op == "2":
        print("Resultado:", subtrair(a, b))
    elif op == "3":
        print("Resultado:", multiplicar(a, b))
    elif op == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opção inválida.")