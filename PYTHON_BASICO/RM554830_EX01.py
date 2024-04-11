#EXERCICIO 01
# Fintech, abreviação de financial technology, refere-se, principalmente, às startups que desenvolvem produtos
# financeiros totalmente digitais, através da utilização intensiva da tecnologia. Aliás, este é o principal diferencial
# das Fintechs em relação às instituições tradicionais do setor financeiro: por meio da tecnologia, disponibilizar aos seus
# clientes os principais produtos do setor financeiro de maneira simples. Neste contexto, desenvolva soluções em Python para
# atender às seguintes necessidades de negócio:

# 1 – A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar suas fontes de receitas,
# gastos, dívidas e investimentos.  Ela precisa realizar uma votação para escolher qual dia da semana é o melhor para a
# realização das lives com o time da mentoria financeira. Desenvolva um programa em que os colaboradores informem um dos 
# 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) da sua preferência para participar
# da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.
# Observação: Verifique o número de colaboradores que irão participar da votação para programar sua estrutura de repetição."

colaboradores = []

preferencias  = {'segunda-feira':0,'terça=feira':0,'quarta-feira':0,'quinta-feira':0,'sexta-feira':0}

#função que ira cadastrar o colaborador e deixar ele escolher um dia da semana para a reunião
def cadastrar_colaborador():
    nome = input("Informe o nome do colaborador: ")
    setor = input("Informe o setor do colaborador: ")
    funcao = input("Informe a função do colaborador: ")
    dia = input("Informe um dos dias da semana para participar da live (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").capitalize()
    while dia not in preferencias.keys():
        print("Dia inválido. Por favor, tente novamente.")
        dia = input("Informe um dos dias da semana para participar da live (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").capitalize()
    preferencias[dia] += 1
    colaboradores.append((nome, setor, funcao, dia))

#nessa função será exibida o resultado da votação
def exibir_resultados():
    print("\nResultados da votação:")
    for dia, votos in preferencias.items():
        print(f"{dia}: {votos} votos")
    print("\nColaboradores que votaram e em qual dia:")
    for nome, setor, funcao, dia in colaboradores:
        print(f"{nome} - {setor} - {funcao} votou em {dia}")
    dia_escolhido = max(preferencias, key=preferencias.get)
    print(f"\nO dia escolhido para a reunião é: {dia_escolhido} com {preferencias[dia_escolhido]} votos")


#programa principal que sera rodado os métodos e fazer o loop para a escolha das opções

while True:
    print("\n1. Cadastrar colaborador")
    print("2. Exibir resultados da votação")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_colaborador()

