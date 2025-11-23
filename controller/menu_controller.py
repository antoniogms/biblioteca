from view.menu_view import MenuView
from controller.livro_controller import LivroController

class MenuController:
    def __init__(self):
        self.view = MenuView()
        self.livro_controller = LivroController()
        
    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == 1:
                pass

            elif opcao == 2:
                self.livro_controller.executar()

            elif opcao == 3:
                self.view.mensagem("\nSaindo do sistema...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")