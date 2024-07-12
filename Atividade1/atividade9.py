#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande,
#cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um
#algoritmo em que o usuário forneça a quantidade de camisetas pequenas,
#médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.

preco_pequena = 10.00
preco_media = 12.00
preco_grande = 15.00

quantidade_pequenas = int(input("Digite a quantidade de camisetas pequenas vendidas: "))
quantidade_medias = int(input("Digite a quantidade de camisetas médias vendidas: "))
quantidade_grandes = int(input("Digite a quantidade de camisetas grandes vendidas: "))

total_pequenas = quantidade_pequenas * preco_pequena
total_medias = quantidade_medias * preco_media
total_grandes = quantidade_grandes * preco_grande

valor_total = total_pequenas + total_medias + total_grandes

print(f"O valor total arrecadado é: R${valor_total:.2f}")
