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
