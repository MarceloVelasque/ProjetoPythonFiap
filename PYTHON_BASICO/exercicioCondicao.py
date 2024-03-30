#condição encadeado
pontuacao = input("inisra a pontuação do cliente: ")
pontuacao = int(pontuacao)
if pontuacao >= 1000:
    print("O cliente tem direito a receber mais 3gb na sua franquia de internt!")
else:
    if pontuacao >= 500:
        print("O cliente tem direito a receber mais de 1,5gb na sua franquia de internet!")
    else:
        if pontuacao >=200:
            print("O cliente tem direito a receber mais de 500mb na sua franquia de internet")
        else: 
            print("O cliente não recebera bônus.")

#----------------------------------------------------------------------------------------
#usando elif que simplifica muito esse exemplo de encadeamento acima:

pontuacao = input("Insira a pontuação do cliente:")
pontuacao = int(pontuacao)
if pontuacao >= 1000:
    print(" o cliente tem direito a receber mais 3gb na sua franquia de internet")
elif pontuacao >=500:
    print("O cliente tem direito a receber mais 1,5gb na sua franquia de internet!")
elif pontuacao >=200:
    print("O cliente tem direito a receber mais 500gb na usa franquia de internet!")
else:
    print("O cliente não receberá bônus.")
     #-----------------------------------------------------------------------------------------
    

    #solicitando os dados do aluno
    email_aluno = input("Informe o e-mail do aluno")
    nota_semestral = input("Informe a nota semestral do aluno:")
    #convertendo a nota para o formato float
    nota_semestral = float(nota_semestral)
    #realizando o teste lógico
    if nota_semestral > 8.5:
        print("ENVIANDO E-MAIL PARA {}".format(email_aluno))
#-----------------------------------------------------------------------------------------------
#solicitando os dados do cliente

valor_compra = input("Informe o valor da compra realizada")
cupom = input("Dgite o Cupom de desconto")
#realizar o teste lógico
if cupom.upper() == "NIVER10":
    #valor de 10% de desconto
    valor_final = float(valor_compra)*0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
    #exibindo o valor final da compra
    print("o valor final da comprea é {}".format(valor_final))