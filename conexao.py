import psycopg2
from psycopg2 import Error

def conectar_banco():
    try:
        conexao = psycopg2.connect(
            host="127.0.0.1",
            database="escola",
            user="postgres",
            password="123456",
            port=5432
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

if __name__ == "__main__":
    conn = conectar_banco()
    if conn:
        print("Conexão realizada com sucesso!")
        conn.close()
    else:
        print("Falha na conexão.")