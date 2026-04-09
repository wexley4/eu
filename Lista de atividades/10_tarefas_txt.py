ARQ = "tarefas.txt"

while True:
    print("\n1) Adicionar  2) Listar  3) Sair")
    op = input("Escolha: ")

    if op == "1":
        tarefa = input("Digite a tarefa: ")
        with open(ARQ, "a", encoding="utf-8") as f:
            f.write(tarefa + "\n")
        print("Tarefa salva.")

    elif op == "2":
        try:
            with open(ARQ, "r", encoding="utf-8") as f:
                linhas = [l.strip() for l in f.readlines() if l.strip()]
            if not linhas:
                print("Sem tarefas.")
            else:
                for i, t in enumerate(linhas, 1):
                    print(f"{i}. {t}")
        except FileNotFoundError:
            print("Ainda não existe tarefas.txt (adicione uma tarefa primeiro).")

    elif op == "3":
        break

    else:
        print("Opção inválida.")