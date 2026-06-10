matriz = []
soma_matriz = 0
diagonal_principal = []

print("Preencha a matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        soma_matriz += valor
        if i == j:
            diagonal_principal.append(valor)
    matriz.append(linha)

print("\nMatriz Exibida:")
for linha in matriz:
    print(linha)

print(f"Soma de todos os elementos: {soma_matriz}")
print(f"Elementos da diagonal principal: {diagonal_principal}\n")