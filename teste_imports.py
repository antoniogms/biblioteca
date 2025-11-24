print("🧪 Testando imports...")

try:
    from models.livro_model import LivroModel
    print("✅ LivroModel importado com sucesso!")
except ImportError as e:
    print(f"❌ Erro importando LivroModel: {e}")

try:
    from controllers.livro_controller import LivroController
    print("✅ LivroController importado com sucesso!")
except ImportError as e:
    print(f"❌ Erro importando LivroController: {e}")

print("🎯 Teste completo!")
