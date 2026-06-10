nota = float(input("Digite a nota do aluno: "))
if nota >= 7.0:
    print("Situação: Aprovado")
elif 5.0 <= nota < 7.0:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
print()
