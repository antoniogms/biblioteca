import psycopg2

class LivroModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )

            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"\nErro ao conectar ao banco de dados: {e}\n")

    def inserir(self, titulo, ano_publicacao, id_autor):
        try:
            if not self.existe_autor(id_autor):
                print("\nNenhum autor encontrado com esse ID.\n")
                return False

            self.cursor.execute("INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES (%s,%s,%s);", (titulo, ano_publicacao, id_autor))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao inserir livro: {e}\n")
            self.conn.rollback()

    def listar(self):
        try:
            self.cursor.execute("SELECT id_livro, titulo, ano_publicacao, nome FROM livro INNER JOIN autor ON livro.id_autor = autor.id_autor ORDER BY id_livro;")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"\nErro ao listar livros: {e}\n")
            return []
        
    def atualizar(self, id_livro, titulo, ano_publicacao, id_autor):
        try:
            if not self.existe_livro(id_livro):
                print("\nNenhum livro encontrado com esse ID.\n")
                return False
            
            if not self.existe_autor(id_autor):
                print("\nNenhum autor encontrado com esse ID.\n")
                return False

            self.cursor.execute("UPDATE livro SET titulo=%s, ano_publicacao=%s, id_autor=%s WHERE id_livro=%s;", (titulo, ano_publicacao, id_autor, id_livro))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao atualizar livro: {e}\n")
            self.conn.rollback()
            return False
        
    def excluir(self, id_livro):
        try:
            if not self.existe_livro(id_livro):
                print("\nNenhum livro encontrado com esse ID.\n")
                return False
            
            self.cursor.execute("DELETE FROM livro WHERE id_livro=%s;", (id_livro,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao excluir o livro: {e}\n")
            self.conn.rollback()
            return False
        
    def existe_autor(self, id_autor):
        try:
            self.cursor.execute("SELECT 1 FROM autor WHERE id_autor=%s;", (id_autor,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print("Erro ao verificar a existência do autor: {e}\n")
            return False
        
    def existe_livro(self, id_livro):
        try:
            self.cursor.execute("SELECT 1 FROM livro WHERE id_livro=%s;", (id_livro,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print("Erro ao verificar a existência do livro: {e}\n")
            return False