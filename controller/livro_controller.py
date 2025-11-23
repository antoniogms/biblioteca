from model.livro_model import LivroModel
from view.livro_view import LivroView

class LivroController:
    def __init__(self):
        self.model = LivroModel()
        self.view = LivroView()

    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == 1:
                titulo, ano_publicacao, id_autor = self.view.cadastrar()
                
                if titulo and ano_publicacao and id_autor:

                    response = self.model.inserir(titulo, ano_publicacao, id_autor)
                    
                    if response:
                        self.view.mensagem("\nLivro cadastrado com sucesso!\n")
                    else:
                        self.view.mensagem("\nNão foi possível cadastrar o livro.\n")


            elif opcao == 2:
                livros = self.model.listar()
                self.view.listar(livros)

            elif opcao == 3:
                id_livro, titulo, ano_publicacao, id_autor = self.view.atualizar()
                if id_livro and titulo and ano_publicacao and id_autor:
                    response = self.model.atualizar(id_livro, titulo, ano_publicacao, id_autor)
                    if response:
                        self.view.mensagem("\nLivro atualizado com sucesso!\n")
                    else:
                        self.view.mensagem("\nNão foi possível atualizar o livro.\n")

            elif opcao == 4:
                id_livro = self.view.excluir()
                if id_livro:
                    response = self.model.excluir(id_livro)
                    if response:
                        self.view.mensagem("\nLivro excluído com sucesso!\n")
                    else:
                        self.view.mensagem("\nNão foi possível excluir o livro.\n")

            elif opcao == 5:
                self.view.mensagem("\nSaindo do sitema...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")

