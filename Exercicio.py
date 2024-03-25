class CaixaEletronico:
    def __init__(self):
        self.saldo = 1000  # Saldo inicial
        self.senha_correta = "1234"  # Senha definida
        self.senha_inserida = False  # Flag para verificar se a senha foi inserida
        
    def sacar(self, valor):
        # Método para realizar um saque
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        # Método para realizar um depósito
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")

    def ver_saldo(self):
        # Método para visualizar o saldo atual
        print(f"Seu saldo atual é de R${self.saldo}.")

    def verificar_senha(self, senha):
        # Método para verificar se a senha está correta
        if not self.senha_inserida:
            # Se a senha ainda não foi inserida, verifica a senha e marca a flag como True
            self.senha_inserida = True
            return senha == self.senha_correta
        else:
            # Se a senha já foi inserida anteriormente, retorna True diretamente
            return True

# Função principal
def main():
    # Instanciação do objeto CaixaEletronico
    caixa = CaixaEletronico()
    while True:
        if not caixa.senha_inserida:
            # Se a senha ainda não foi inserida, solicita que o usuário a insira
            senha = input("Digite sua senha (ou 'sair' para sair): ")
            
            if senha.lower() == "sair":
                # Se o usuário digitar 'sair', encerra o programa
                print("Obrigado por usar nosso caixa eletrônico. Até logo!")
                break
            
            if not caixa.verificar_senha(senha):
                # Se a senha inserida estiver incorreta, solicita que o usuário tente novamente
                print("Senha incorreta. Tente novamente.")
                continue
        
        # Menu de operações disponíveis
        print("\nEscolha a operação:")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Ver saldo")
        print("4. Sair")
        opcao = input("Digite o número da operação desejada: ")

        # Executa a operação escolhida pelo usuário
        if opcao == "1":
            valor = float(input("Digite o valor que deseja sacar: "))
            caixa.sacar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor que deseja depositar: "))
            caixa.depositar(valor)
        elif opcao == "3":
            caixa.ver_saldo()
        elif opcao == "4":
            # Encerra o programa
            print("Obrigado por usar nosso caixa eletrônico. Até logo!")
            break
        else:
            # Se a opção inserida pelo usuário for inválida, solicita que ele tente novamente
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    # Chama a função principal quando o script é executado
    main()
