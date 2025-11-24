import psycopg2
print("TESTE FINAL")
print("=" * 30)

# Teste de conexão direta

try:
    conn = psycopg2.connect(
        host="localhost",
        database="biblioteca_mvc",
        user="postgres",
        password="admin123",
        port="5432"
    )
    print("Conexão direta: OK")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM autor")
    total = cursor.fetchone()[0]
    print(f"Autores no banco: {total}")

    cursor.close()
    conn.close()

    # Teste do sistema
    from main import BibliotecaApp
    print("Sistema principal: OK")

    print("\nTUDO PRONTO! Execute: python main.py")

except Exception as e:
    print(f"ERRO: {e}")

