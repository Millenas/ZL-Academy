#A padaria Hotpão vende uma certa quantidade de pães franceses e uma
#quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa
#R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos
#pães e broas (juntos), e quanto deve guardar numa conta de poupança (10%
#do total arrecadado). Você foi contratado para fazer os cálculos para o dono.
#Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e
#de broas, e depois calcular os dados solicitados.

preco_pao = 0.12   # em reais (R$)
preco_broa = 1.50  # em reais (R$)

quantidade_paes = int(input("Digite a quantidade de pães vendidos hoje: "))
quantidade_broas = int(input("Digite a quantidade de broas vendidas hoje: "))

total_arrecadado = (quantidade_paes * preco_pao) + (quantidade_broas * preco_broa)

valor_poupanca = total_arrecadado * 0.10

print(f"Valor arrecadado com a venda dos pães e broas: R${total_arrecadado:.2f}")
print(f"Valor a ser guardado na poupança: R${valor_poupanca:.2f}")
