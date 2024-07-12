#Entrar com o dia e o mês de uma data e informar quantos dias se passaram
#desde o início do ano. Esqueça a questão dos anos bissextos e considere
#sempre que um mês possui 30 dias.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

dias_passados = (mes - 1) * 30 + dia

print(f"Desde o início do ano, passaram-se {dias_passados} dias.")