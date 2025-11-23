from view.menu_view import MenuView

class MenuController:
    def __init__(self):
        self.view = MenuView()
        
    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == 1:
                pass

            elif opcao == 2:
                pass

            elif opcao == 3:
                self.view.mensagem("\nSaindo do sistema...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")