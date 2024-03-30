#assim é criada uma lista abrindo e fechando []
intrumentos = []
#o append adiciona sempre o valor no final
#criação de uma lista com os nomes dos jedi
jedi = ["YODA", "LUKE", "OBI-WAN", "ANAKIN"]
#incluindo um valor no final da lista
jedi.append(input("DIGITE UM NOME PARA POR NA LISTA"))
#a variavel assumirácada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)
#-------------------------------------------------------
#aqui estamos inserindo na lista na posição 2 o valor LUMINARA
    #criação de uma lista com os nomes dos jedi
jedi = ["YODA", "LUKE", "OBI-WAN", "ANAKIN"]
#incluindo um valor no final da lista
jedi.insert(2, "lUMINARA")
#a variavel assumirácada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)
#-------------------------------------------------------
#aqui estamos usando o insert de uma forma que o usuário digite já definido a posição 
#criação de uma lista com os nomes dos jedi
jedi = ["YODA", "LUKE", "OBI-WAN", "ANAKIN"]
#incluindo um valor no final da lista
jedi.insert(2,input("DIGITE UM NOME PARA POR NA LISTA"))
#a variavel assumirácada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)    
#-------------------------------------------------------

#para remover o último item da lista basta usar o pop exemplo jedi.pop()

#criação de uma lista com os nomes dos jedi
jedi = ["YODA", "LUKE", "OBI-WAN", "ANAKIN"]
#removendo o último valor inserido na lista
jedi.pop()
#a variavél assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta o loop, exibir o valor assumido
    print(nome)
#-------------------------------------------------------
#para remover um em especifico basta colocar o valor do indice exemplo pop.(2) removendo assim o valor da lista da posição 2

#criação de uma lista com os nomes dos jedi
jedi = ["YODA", "LUKE", "OBI-WAN", "ANAKIN"]
#removendo o último valor inserido na lista
jedi.pop(2)
#a variavél assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta o loop, exibir o valor assumido
    print(nome)
#-------------------------------------------------------
#para simplifcar isso exite um recurso no python o remove, aonde é só chamar o remove.("YODA")
#criação de uma lista com os nomes dos jedi
jedi = ["YODA", "LUKE", "OBI-WAN", "ANAKIN"]
#removendo o último valor inserido na lista
jedi.remove("YODA")
#a variavél assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta o loop, exibir o valor assumido
    print(nome)

#-------------------------------------------------------
#existem alguns métodos muito úteis para manipulação de listas para usar no dia a dia que são eles:
#count()
#sort()
#reverse()
#exemplo:

#valores fora de ordem

valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]
#exibição da lista
print("a lista foi criada assim: {}".format(valores))
#contagem de elementos
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes".format(contagem))
#invertendo a lista
valores.reverse
print("A lista agora está invertida: {}".format(valores))
#ordenar a lista
valores.sort()
print("a lista afora está ordenada: {}".format(valores))
#-------------------------------------------------------
# existe outras funções que também podem ajudar como o:
#len
#sum
#exemplo:

#valores de uma lista
valores = [2, 3, 5, 10]
#tamanho da lista
tamanho = len(valores)
print("A lista tem {} elementos".format(tamanho))
#a soma dos elementos
soma = sum(valores)
print("A soma dos elementos é {}".format(soma))

#-------------------------------------------------------
#EXERCICIO BÁSICO

#estrutura do menu

opcao = -1
notas = []
while opcao != 4:
    print("1-Cadastrar nota\n2-Cadastrar nota\n3-Calcular média\n1-Sair")
    opcao = int(input("Informe a opção desejada:"))
if opcao == 1:
    nota = float(input("Por favor informe a nota do aluno"))
    notas.append(nota)

elif opcao == 2:
    print("AS NOTAS DA TURMA SÃO:")
    for nora in notas:
        print(notas)

elif opcao == 3:
    media = sum(notas) / len(notas)


elif opcao == 4:
    print("Saindo!")
else:
    print("Opção invalida")
#-------------------------------------------------------