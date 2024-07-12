def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar um número ao vetor")
    print("2. Remover um número do vetor")
    print("3. Exibir o vetor completo")
    print("4. Encontrar e exibir o maior e o menor número no vetor")
    print("5. Calcular e exibir a soma de todos os números no vetor")
    print("6. Sair")

def adicionar_numero(vetor):
    try:
        num = int(input("Digite o número para adicionar ao vetor: "))
        vetor.append(num)
        print(f"{num} foi adicionado ao vetor.")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_numero(vetor):
    try:
        num = int(input("Digite o número para remover do vetor: "))
        if num in vetor:
            vetor.remove(num)
            print(f"{num} foi removido do vetor.")
        else:
            print("Número não encontrado no vetor.")
    except ValueError:
        print("Por favor, digite um número válido.")

def exibir_vetor(vetor):
    print("Vetor completo:", vetor)

def encontrar_maior_menor(vetor):
    if vetor:
        maior = vetor[0]
        menor = vetor[0]
        for num in vetor:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        print(f"Maior número no vetor: {maior}")
        print(f"Menor número no vetor: {menor}")
    else:
        print("O vetor está vazio.")

def calcular_soma(vetor):
    soma = 0
    for num in vetor:
        soma += num
    print(f"Soma de todos os números no vetor: {soma}")

def main():
    vetor = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_numero(vetor)
        elif opcao == "2":
            remover_numero(vetor)
        elif opcao == "3":
            exibir_vetor(vetor)
        elif opcao == "4":
            encontrar_maior_menor(vetor)
        elif opcao == "5":
            calcular_soma(vetor)
        elif opcao == "6":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
