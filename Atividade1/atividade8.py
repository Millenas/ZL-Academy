#Faça um algoritmo para ler três notas de um aluno em uma disciplina e
#imprimir a sua média ponderada (as notas tem pesos respectivos de 1, 2 e 3).

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

peso1 = 1
peso2 = 2
peso3 = 3

media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f"A média ponderada das notas é: {media_ponderada:.2f}")
