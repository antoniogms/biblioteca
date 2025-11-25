class LivroView:
    @staticmethod
    def menu():
        print("\n--------- GERENCIADOR LIVRO ---------\n")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Voltar ao menu principal")

        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
        return -1

    @staticmethod
    def cadastrar():
        try:
            titulo = input("Título do livro: ")
            ano_publicacao = int(input("Ano de publicação: "))
            id_autor = int(input("ID do autor: "))
            return titulo, ano_publicacao, id_autor
        except ValueError:
            print("\nEntrada inválida. Tente novamente.\n")
            return None, None, None

    @staticmethod
    def listar(livros):
        if not livros:
            print("\nNenhum livro cadastrado.\n")
        else:
            print("\n-------- Lista de Livros ---------\n")
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Ano de publicação: {livro[2]} | Autor: {livro[3]}")

    @staticmethod
    def atualizar():
        try:
            id_livro = int(input("ID do livro a atualizar: "))
            titulo = input("Novo título: ")
            ano_publicacao = int(input("Novo ano de publicação: "))
            id_autor = int(input("Novo ID do autor: "))
            return id_livro, titulo, ano_publicacao, id_autor
        except ValueError:
            print("\nEntrada inválida. Tente novamente.\n")
            return None, None, None, None

    @staticmethod  
    def excluir():
        try:
            id_livro = int(input("\nID do livro a excluir: "))
            return id_livro
        except ValueError:
            print("\nEntrada inválida.\n")
            return None

    @staticmethod
    def mensagem(msg):
        print(msg)