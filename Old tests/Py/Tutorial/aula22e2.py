t = int(input("Insira o número de turmas: "))
print("")

soma = 0
for i in range(1,t+1):
    x = int(input("Digite o número de alunos da turma %d: "%i))

    while x < 0 or x > 40:
        print("Quantidade de alunos inválida!")
        x = int(input("Digite o número de alunos da turma %d: "%i))
    soma += x

media = soma/t
print("")
print("Número médio de alunos é %g"%media)
