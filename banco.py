import psycopg2

def conectar():
    try:
        # Estabelece a conexão ao banco de dados
        conexion = psycopg2.connect(
            host="localhost",
            database="compras",
            user="postgres",
            password="1234"
        )
        return conexion
    except Exception as e:
        print(f"Não foi possivel conectar ao Banco de Dados: {e}")
        return None

