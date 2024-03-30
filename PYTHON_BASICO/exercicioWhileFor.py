#Qual a  resposta para a vida, o universo e tudo mais?
#criação da variavel com um valor inicial

resposta = "0"
#enquanto a resposta não for 42, a repetição ocorre
while(resposta != "42"):
# para cada uma das repetições, o usuário vai submeter uma resposta
    resposta = input("QUAL A RESPOSTA PARA A VIDA, O UNIVERSO E TUDO MAIS?")
    #quando o laço terminar, a mensagem é eixibida
    print("parabéns, você acertou!")
    #-------------------------------------------------------------------------
    contadora = 0
    while contadora < 100:
        print(contadora)
    contadora = contadora+1
    #-------------------------------------------------------------------------
    #tabuada
    i = 1
    numero = int(input("por favor, informe o valor do qual deseja a tabuada"))

    while i <= 10:
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
        contadora = contadora + 1
    #--------------------------------------------------------------------------
    # um pouco de como funciona o FOR no python
        for contadora in range(10): #range faz um intervalo de 0 a 9 na nossa variavel contadora
            print(contadora)
    #-------------------------------------
    # caso queira começar contando apartir de um valor especifico  e não de zero pode ser colocado dentro do range 
        for contadora in range(3,10):#dentro no range coloquei 3 que vai começar a contar apartir do 3 e ir até 09 ou 10
            print(contadora)
    #-------------------------------------
    #nesse exemplo podemos usar no ranger(2,11,2) que seria começar no 2 contar até 11 que no caso seria até 10 , pulando de 2 em 2
        for contadora in range(2,11,2):
            print(contadora)
    #--------------------------------------
    # mesmo exemplo acima só que fazendo uma tabuada
    numero = int(input("digite o valor do qual deseja obeter a tabuada "))

    for contadora in range(1,11,1):
        print(contadora * numero)    
    #---------------------------------------------------------------------------------------------------------------------------
    #a variavel servira para receber a opção do usuário
    opcao = -1  
    #enquanto o usuário não digitar a opção de sáida
    while opcao !=4:
        #exibição das opçẽs do menu
        print("SUPER PROGRAMA MARAVILHOSO")
        print("1 - Rodar código 1")
        print("2 - Rodar código 2")
        print("3 - Rodar código 3")
        print("4- Sair do programa")
        opcao = int(input("Informe sua opção: "))
    #verificar das opções disponíveis
        if opcao == 1:
            print("CÓDIGO 1 RODANDO!")
        elif opcao ==2:
            print("CÓDIGO 2 RODANDO!")
        elif opcao == 3:
            print("CÓDIGO 3 RODANDO!")
        #quando o looping terminar de rodar, exibe essa mensagem
            print("OK! o programa está encerrado....")
    #-------------------------------------------------------------------------------------------------------------------------------
    # variavel para armazenar o peso total das caixas
    peso_total = 0.0
    #loop para repetir por 100 vezes a solicitação de peso
    for x in range(1,101):
        #para cada volta do loop, solicitar o peso da caixa
        peso_atual = float(input("informe o peso da caixa atual:"))
        #para cada peso solicitado, somar o peso total
        peso_total = peso_total + peso_atual
    #ao final do loop, calcular a média aritmética
        media = peso_total/100
        #exibeção dos resultados!
        print(f"O peso total de caixas é {}.A média de peso é {}".format(peso_total, media))
    #-------------------------------------------------------------------------------------------------------------------------------
        
        #LISTA DE EXERCICIOS DO CAPITULO 03

        #01)
        #Você deve elaborar um algoritimo implementado em python em que o usuário informe quantos alimentos consumiu naquele dia e depois
        #possa informar o número de calorias de cada um dos alimentos.
        #como não estudamos listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas, más deve exibir o total de calorias no final.

        quantidade_alimentos = int(input("Por favor, informe quantos alimentos você consumiu hoje"))
        total_calorias = 0
        for alimento in range(1,quantidade_alimentos +1,1):
            caloria = int(input("Informe a quantidade de calorias do {} alimento".format(alimento)))
            print(alimento)
            total_calorias = total_calorias + caloria
        
            print("Foram consumidas {} calorias ao longo do dia".format(total_calorias))
        #----------------------------------------------------------------------------------------------
        #02)
        #Olhando para o mercado de edicação infantil, você e sua equipe decidem criar um aplicativo onde as ciranças apreendem a controlar
        #os seus gastos. Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar 
        #QUANTAS TANSAÇÕES  financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que 
        #realizou. Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.
        
        quantidade_transacoes = int(input("Informe a quantidade de transações"))
        for n_transacao in range(1, quantidade_transacoes + 1, 1):
            transacao = float(input("Por favor informe a transação de número {}".format(n_transacao)))
            total_transacoes = total_transacoes + transacao

            media = total_transacoes / quantidade_transacoes
            print("Neste dia foi gasto um total de R${}, com uma média de R${} por transação".format(total_transacoes,media))
        #-------------------------------------------------------------------------------------------------
        #03)
        #Uma grande empresa de jogos está querendo tornar seus games mais desafiadore. Por isso ela contratou você para desenvolver um
        #algoritmo que será aplicado futuramente em diversos outros games: o algoritmo da sorte de fibonnaci.
        # A ideia dessa empresa, claro é fazer com que seja mais difícil os jagores terem sucesso nas ações que realizam nos games. Por
        #isso o seu algoritmo deverá funcionar da seguinte forma: o usuário deve digitar um valor numérico inteiro e o algoritmo
        #deverá verificar se esse valor encontra-se n sequência de Fibonnaci. Caso o número esteja na sequência, o algoritmo deve
        #exibir a mensagem "Ação bem sucedida!" e, caso não esteja, deve exibir a mensagem "A ação falhou...".
        
        numero_usuario = int(input("Por favor, informe um nṹmero"))
        quantidade_elemento = 5
        anterior1 = 1
        anterior2 = 0
        for n_elemento in range(1, numero_usuario +1,1):
            atual = anterior1 + anterior2
            anterior1 = anterior2
            anterior2 = atual
           
        if numero_usuario == atual:
                print("Ação bem sucedida")
                break
        elif numero_usuario < atual:
                print("ação falhou")
                break
    #---------------------------------------------------------------------------------------------------------------------------------------
    