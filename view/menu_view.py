class MenuView:
    @staticmethod
    def menu():
        print("\n--------- MENU PRINCIPAL ---------\n")
        print("1. Gerenciar autor")
        print("2. Gerenciar livro")
        print("3. Sair")

        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
            return -1
        
    @staticmethod
    def mensagem(msg):
        print(msg)