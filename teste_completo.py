print("🎯 TESTE COMPLETO DO SISTEMA")
print("=" * 40)

# Testar cada parte do sistema
try:
    # 1. Testar database
    from models.database import Database
    db = Database()
    conn = db.connect()
    if conn:
        print("✅ Database: OK")
        db.disconnect()
    else:
        print("❌ Database: FALHOU")
        exit()

    # 2. Testar modelos
    from models.autor_model import AutorModel
    from models.livro_model import LivroModel

    autor_model = AutorModel()
    livro_model = LivroModel()
    print("✅ Models: OK")

    # 3. Testar controllers
    from controllers.autor_controller import AutorController
    from controllers.livro_controller import LivroController

    autor_controller = AutorController()
    livro_controller = LivroController()
    print("✅ Controllers: OK")

    # 4. Testar views
    from views.autor_view import AutorView
    from views.livro_view import LivroView
    from views.menu_view import MenuView

    autor_view = AutorView()
    livro_view = LivroView()
    menu_view = MenuView()
    print("✅ Views: OK")

    # 5. Testar listagens
    autores = autor_controller.listar_autores()
    livros = livro_controller.listar_livros()

    print(f"✅ Autores no banco: {len(autores)}")
    print(f"✅ Livros no banco: {len(livros)}")

    print("\n🎉 SISTEMA COMPLETO FUNCIONANDO!")
    print("👉 Agora execute: python main.py")

except Exception as e:
    print(f"❌ ERRO NO TESTE: {e}")
