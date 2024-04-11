def exibir_tabela_imposto():
    print("Tabela de Impostos de Renda para Resgate de Investimentos:")
    print("-" * 80)
    print("| Período de Investimento | Alíquota de IR |")
    print("|------------------------|----------------|")
    print("| Até 180 dias            | 22,5%          |")
    print("| De 181 a 360 dias       | 20%            |")
    print("| De 361 a 720 dias       | 17,5%          |")
    print("| Acima de 720 dias       | 15%            |")
    print("-" * 80)

def calcular_imposto_de_renda(dias_investido):
    if dias_investido <= 180:
        aliquota = 0.225
    elif dias_investido <= 360:
        aliquota = 0.20
    elif dias_investido <= 720:
        aliquota = 0.175
    else:
        aliquota = 0.15
    return aliquota

def main():
    exibir_tabela_imposto()
    tipo_investimento = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
    valor_investido = float(input("Digite o valor investido: "))
    dias_investido = int(input("Digite o número de dias que o valor permaneceu investido: "))

    # Supondo uma taxa de rendimento simples de 1% ao ano para simplificar o exemplo
    taxa_rendimento = 0.01
    rendimento = valor_investido * (1 + taxa_rendimento)**dias_investido

    print("\nResultado do Rendimento:")
    print("-" * 80)
    print(f"Valor Investido: R$ {valor_investido:.2f}")
    print(f"Dias Investidos: {dias_investido} dias")
    print(f"Rendimento: R$ {rendimento:.2f}")
    print("-" * 80)

    valor_resgate = float(input("Digite o valor a ser resgatado: "))
    aliquota = calcular_imposto_de_renda(dias_investido)
    imposto = valor_resgate * aliquota

    print("\nResultado do Imposto de Renda:")
    print("-" * 80)
    print(f"Valor a Ser Resgatado: R$ {valor_resgate:.2f}")
    print(f"Imposto de Renda: R$ {imposto:.2f}")
    print("-" * 80)

if __name__ == "__main__":
    main()
