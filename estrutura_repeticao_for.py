soma_for = 0
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    soma_for += num
media_for = soma_for / 5
print(f"Soma: {soma_for} | Média: {media_for}\n")
