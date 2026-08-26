from banco import conectar


conexao = conectar()
cursor = conexao.cursor()

nome = input("Nome do produto: ")
quantidade = int(input("Quantidade: "))

cursor.execute("""
    INSERT INTO produtos (nome, quantidade)
    VALUES (%s, %s)
""", (nome, quantidade))

conexao.commit()

print("Produto adicionado!")

cursor.close()
conexao.close()