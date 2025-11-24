import os
print("VERIFICANDO TODOS OS ARQUIVOS...")
print("=" * 40)

# Verificar se todos os arquivos existem

arquivos_necessarios = [
    'models/database.py',
    'models/autor_model.py',
    'models/livro_model.py',
    'controllers/autor_controller.py',
    'controllers/livro_controller.py',
    'views/menu_view.py',
    'views/autor_view.py',
    'views/livro_view.py',
    'main.py'
]

for arquivo in arquivos_necessarios:
    if os.path.exists(arquivo):
        print(f"{arquivo}")
    else:
        print(f"{arquivo} - FALTANDO!")

print("\n🧪 TESTANDO IMPORTS...")

try:
    from models.database import Database
    from models.autor_model import AutorModel
    from models.livro_model import LivroModel
    from controllers.autor_controller import AutorController
    from controllers.livro_controller import LivroController
    from views.menu_view import MenuView
    from views.autor_view import AutorView
    from views.livro_view import LivroView
    from main import BibliotecaApp
    print("TODOS OS IMPORTS OK!")
except Exception as e:
    print(f"ERRO NOS IMPORTS: {e}")

print("\nPRONTO PARA EXECUTAR!")

