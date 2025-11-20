import psycopg2

class AutorModel:
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

    def listar(self):
        try:
            self.cursor.execute("SELECT * FROM autor ORDER BY id_autor;")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"\nErro ao listar produtos: {e}\n")
            return []
    
    def inserir(self, nome, nacionalidade):
        try:
            self.cursor.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s,%s);", (nome, nacionalidade))
            self.conn.commit()
        except Exception as e:
            print(f"\nErro ao inserir autor: {e}\n")
            self.conn.rollback()

    def existe_id(self, id_autor):
        try:
            self.cursor.execute("SELECT 1 FROM autor WHERE id_autor=%s;", (id_autor,))
            return self.cursor.fetchone is not None
        except Exception as e:
            print(f"\n Erro ao verificar a existência do autor: {e}\n")
            return False
        
    def atualizar(self, id_autor, nome, nacionalidade):
        try:
            if not self.existe_id(id_autor):
                print("\nNenhum autor encontrado com esse ID.\n")
                return False
            
            self.cursor.execute("UPDATE autor SET nome=%s, nacionalidade=%s WHERE id_autor=%s", (nome, nacionalidade, id_autor))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao atualizar produto: {e}\n")
            self.conn.rollback()
            return False
        
    def excluir(self, id_autor):
        try:
            if not self.existe_id(id_autor):
                print("\nNenhum autor encontrado com esse ID.\n")
                return False
            
            self.cursor.execute("DELETE FROM autor WHERE id_autor=%s;", (id_autor,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao excluir autor: {e}\n")
            self.conn.rollback()
            return False
        
    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()