#------------------------------------------------------------------------------------
#EXERCICIO 02
# A compra de um veículo pode ser realizada parcelada.
# Crie um programa que receba o valor de um carro e mostre  com os seguintes dados:
# preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
# a) O preço final para compra à vista tem um desconto de 20%:
# b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60

def calcular_preco_final(valor_carro):
    return valor_carro * 0.8 # Desconto de 20%

percentual_acrescimo = {
    6: 0.03,
    12: 0.06,
    18: 0.09,
    24: 0.12,
    30: 0.15,
    36: 0.18,
    42: 0.21,
    48: 0.24,
    54: 0.27,
    60: 0.30
}

def calcular_valor_parcela(valor_final):
    for quantidade_parcelas, percentual in percentual_acrescimo.items():
        valor_parcela = valor_final * (1 + percentual) / quantidade_parcelas
        print(f"Parcelas: {quantidade_parcelas}, Valor da Parcela: R$ {valor_parcela:.2f}")

def main():
    while True:
        # Solicitar ao usuário o valor do carro
        valor_carro = float(input("Digite o valor do carro (ou '0' para sair): "))
        if valor_carro == 0:
            break

        # Aqui é calculado o preço final com desconto para compra à vista
        preco_final = calcular_preco_final(valor_carro)

        # aqui é Calculado e exibir o valor da parcela para todas as opções de quantidade de parcelas
        print("Valores das Parcelas:")
        calcular_valor_parcela(preco_final)

        # É solicitado ao usuário a quantidade de parcelas desejada
        quantidade_parcelas = int(input("Digite a quantidade de parcelas desejada (6, 12, 18, 24, 30, 36, 42, 48, 54, 60): "))

        # Calculo do valor da parcela com o percentual de acréscimo correspondente
        valor_parcela = preco_final * (1 + percentual_acrescimo[quantidade_parcelas]) / quantidade_parcelas

        # Exibir os resultados
        print(f"\nPreço final com desconto para compra à vista: R$ {preco_final:.2f}")
        print(f"Quantidade de parcelas escolhida: {quantidade_parcelas}")
        print(f"Valor da parcela escolhida: R$ {valor_parcela:.2f}")

        # Perguntar ao usuário se ele deseja continuar
        continuar = input("Digite 's' para continuar ou qualquer outra tecla para sair: ")
        if continuar.lower() != 's':
            break

# Executar o programa
main()
