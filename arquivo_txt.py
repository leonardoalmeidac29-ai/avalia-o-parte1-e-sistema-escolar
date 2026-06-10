nome_aluno_txt = input("Digite o nome do aluno para salvar no arquivo: ")
with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(nome_aluno_txt + "\n")
print("Informação gravada com sucesso em 'alunos.txt'.\n")
