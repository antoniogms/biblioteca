from views.menu_view import MenuView
from views.autor_view import AutorView
from views.livro_view import LivroView


class BibliotecaApp:
    def __init__(self):
        self.menu_view = MenuView()
        self.autor_view = AutorView()
        self.livro_view = LivroView()

    def executar(self):
        print("Bem-vindo ao Sistema Biblioteca Universitária!")

        while True:
            opcao = self.menu_view.mostrar_menu_principal()

            if opcao == '1':
                self.gerenciar_autores()
            elif opcao == '2':
                self.gerenciar_livros()
            elif opcao == '3':
                print("\nSaindo do sistema... Até logo!")
                break
            else:
                print("\nOpção inválida! Tente novamente.")

    def gerenciar_autores(self):
        while True:
            opcao = self.menu_view.mostrar_menu_autor()

            if opcao == '1':
                self.autor_view.cadastrar_autor()
            elif opcao == '2':
                self.autor_view.listar_autores()
            elif opcao == '3':
                self.autor_view.atualizar_autor()
            elif opcao == '4':
                self.autor_view.excluir_autor()
            elif opcao == '5':
                break
            else:
                print("\nOpção inválida! Tente novamente.")

    def gerenciar_livros(self):
        while True:
            opcao = self.menu_view.mostrar_menu_livro()

            if opcao == '1':
                self.livro_view.cadastrar_livro()
            elif opcao == '2':
                self.livro_view.listar_livros()
            elif opcao == '3':
                self.livro_view.atualizar_livro()
            elif opcao == '4':
                self.livro_view.excluir_livro()
            elif opcao == '5':
                break
            else:
                print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    app = BibliotecaApp()
    app.executar()
