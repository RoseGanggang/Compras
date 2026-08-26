from banco import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

cursor.close()
conexao.close()

