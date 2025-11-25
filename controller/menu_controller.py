from view.menu_view import MenuView
from controller.autor_controller import AutorController
from controller.livro_controller import LivroController

class MenuController:
    def __init__(self):
        self.view = MenuView()
        self.autor_controller = AutorController()
        self.livro_controller = LivroController()
        
    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == 1:
                self.autor_controller.executar()
            elif opcao == 2:
                self.livro_controller.executar()

            elif opcao == 3:
                self.view.mensagem("\nSaindo do sistema...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")