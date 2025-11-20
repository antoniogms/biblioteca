class AutorView:
    @staticmethod
    def menu():
        print("\n--------- MENU DE AUTORES ---------\n")
        print("1. Cadastrar autor")
        print("2. Listar autores")
        print("3. Atualizar autor")
        print("4. Excluir autor")
        print("5. Voltar ao menu principal")

        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
            return -1
        
    @staticmethod
    def listar(autores):
        if not autores:
            print("\nNenhum autor cadastrado.\n")
        else:
            print("\n--------- Lista de Autores ---------\n")
            for autor in autores:
                print(f"ID: {autor[0]} | Nome: {autor[1]} | Nacionalidade {autor[2]}")

    @staticmethod
    def cadastrar():
        nome = input("Nome do autor: ")
        nacionalidade = input("Nacionalidade:")

        return nome, nacionalidade
    
    @staticmethod
    def atualizar():
        try:
            id_autor = int(input("ID do autor a atualizar: "))
            nome = input("Novo nome: ")
            nacionalidade = input("Nova nacionalidade: ")

            return id_autor, nome, nacionalidade
        
        except ValueError:
            print("\nEntrada inválida.\n")
            return None, None, None
        
    @staticmethod
    def excluir():
        try:
            id_autor = int(input("ID do autor a excluir: "))
            return id_autor
        except ValueError:
            print("\nEntrada inválida.\n")
            return None
        
    @staticmethod
    def mensagem(msg):
        print(msg)