#Construa um algoritmo para calcular o IMC (Índice de Massa Corporal) de uma pessoa.

peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura ** 2)

print(f"O seu IMC é: {imc:.2f}")

#Exibe a classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"A classificação do seu IMC é: {classificacao}")
