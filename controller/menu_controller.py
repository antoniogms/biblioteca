from view.menu_view import MenuView
from controller.autor_controller import AutorController

class MenuController:
    def __init__(self):
        self.view = MenuView()
        self.controller = AutorController()

    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == 1:
                self.controller.executar()

            elif opcao == 2:
                pass

            elif opcao == 3:
                self.view.mensagem("\nSaindo do sistema...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")