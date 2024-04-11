#funções em python básica
def somar():
    valor1 = int(input("DIgite um valor!"))
    valor2 = int(input("digite o segundo valor"))
soma = valor1 + valor2
print(soma)

somar()

#------------------------------------------------------
#função com parametro

#Função que calcula a velocidade média

def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} Km/h".format(velocidade_media))

#aqui começa o programa principal

distancia = float(input("Informe a distância"))
tempo = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
calcularVelocidadeMedia(distancia,tempo)

#chamaa função com valores definidos pelo programador
calcularVelocidadeMedia(15,2)
#------------------------------------------------------

#função com return:
def calcularVelocidadeMedia2(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
   return velocidade_media

distancia = float(input("Informe a distância"))
tempo = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
print("A velocidade média é {}".format(calcularVelocidadeMedia2(distancia,tempo)))

#----------------------------------------------------------------------------------------

#função de soma
def somar(a,b):
    return float(a) + float(b)


#função de subtração
def subtrair(a,b):
    return float(a) + float(b)

#função de divisão
def dividir(a,b):
    return float(a) + float(b)

#função de multiplicação
def dividir(a,b):
    return float(a) + float(b)

op = -1
while (op != 5):
    print("1 = somar dois valores")
    print("2 = subtrair dois valores")
    print("3 = dividir dois valores")
    print("4 = multiplicar dois valores")
    print("5 = ssair")
    op = int(input("Digite a sua opção!"))

    if op ==1:
        print(somar(float(input("Digite o primeiro valor:")),float(input("Digite o segundo valor"))))
    elif op ==2:
        print(subtrair(float(input("Digite o primeiro valor:")),float(input("Digite o segundo valor"))))
    elif op == 3:
        print(dividir(float(input("Digite o primeiro valor:")),float(input("Digite o segundo valor"))))
    elif op ==4:
        print(multiplicacao(float(input("Digite o primeiro valor:")),float(input("Digite o segundo valor"))))
    elif op == 5:
        print("Saindo")
    else:
        print("Opção inválida")