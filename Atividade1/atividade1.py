#A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo
#para ler as dimensões de um terreno e depois exibir a área do terreno.

largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))

area = largura * comprimento

print(f"A área do terreno é: {area:.2f} metros quadrados")
