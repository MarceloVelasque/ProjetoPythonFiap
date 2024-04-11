#EXERCICIO 03
# Na oferta de um produto de crédito aos clientes, três informações são muito importantes apresentar ao cliente:
# valor da dívida, a taxa de juros e o número de parcelas para pagamento do empréstimo contraído junto à Fintech. 
# Faça um programa que receba o valor de uma dívida  e mostre uma tabela  com os seguintes dados:
# Valor da dívida, valor do juros, quantidade de parcelas e valor da parcela.

def calcular_valor_juros(valor_divida, percentual_juros):
    return valor_divida * percentual_juros / 100

def calcular_valor_parcela(valor_divida, percentual_juros, quantidade_parcelas):
    juros = calcular_valor_juros(valor_divida, percentual_juros)
    return (valor_divida + juros) / quantidade_parcelas

def exibir_menu():
    print("1. Digitar o valor da dívida")
    print("2. Sair")
    return int(input("Escolha uma opção: "))

def exibir_resultados(valor_divida):
    quantidades_parcelas = [1, 3, 6, 9, 12]
    percentuais_juros = [0, 10, 15, 20, 25]
    print(f"Digite o valor da dívida: {valor_divida:.2f} Total: R$ {valor_divida:.2f}")
    for quantidade_parcelas in quantidades_parcelas:
        for percentual_juros in percentuais_juros:
            valor_juros = calcular_valor_juros(valor_divida, percentual_juros)
            valor_parcela = calcular_valor_parcela(valor_divida, percentual_juros, quantidade_parcelas)
            print(f"{percentual_juros:.1f}% de Juros: R$ {valor_juros:.2f} Total: R$ {valor_juros + valor_divida:.2f}")
            print(f"Número de parcelas: {quantidade_parcelas} Valor da Parcela: R$ {valor_parcela:.2f}")
            print("-" * 60) # Linha de separação

def main():
    while True:
        opcao = exibir_menu()
        if opcao == 1:
            valor_divida = float(input("Digite o valor da dívida: "))
            exibir_resultados(valor_divida)
        elif opcao == 2:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
