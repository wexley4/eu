n = int(input("Quantidade N: "))

if n <= 0:
    print("N deve ser maior que 0.")
else:
    nums = []
    for i in range(n):
        nums.append(float(input(f"Número {i+1}: ")))

    print("Maior:", max(nums))
    print("Menor:", min(nums))
    print("Média:", sum(nums) / len(nums))