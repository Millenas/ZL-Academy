#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um
#algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir
#quantos litros ele conseguiu colocar no tanque.

preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_pagamento = float(input("Digite o valor do pagamento: "))

quantidade_litros = valor_pagamento / preco_litro

print(f"Com {valor_pagamento} reais, você conseguiu colocar {quantidade_litros:.2f} litros de gasolina no tanque.")
