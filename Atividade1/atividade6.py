#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.
#Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos)
#e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

preco_por_quilo = 12.00
peso_prato = float(input("Digite o peso do prato montado (em quilos): "))

valor_a_pagar = peso_prato * preco_por_quilo

print(f"O valor a pagar é R${valor_a_pagar:.2f}")
