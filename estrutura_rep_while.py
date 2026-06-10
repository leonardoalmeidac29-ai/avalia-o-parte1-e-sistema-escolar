soma_while = 0
quantidade = 0
while True:
    num = float(input("Digite un número (ou 0 para sair): "))
    if num == 0:
        break
    soma_while += num
    quantidade += 1
print(f"Quantidade de números digitados: {quantidade} | Soma total: {soma_while}\n")
