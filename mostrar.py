from banco import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()

def mostrar_produtos():

    print("\n" + "=" * 57)
    print(f"|  {'ID':<18} {'PRODUTO':<23} {'QTD':>8}  |")
    print("=" * 57)

    for produto in produtos:
        print(f"|  {produto[0]:<10} {produto[1]:<30} {produto[2]:>8}   |")

    print("=" * 57)

cursor.close()
conexao.close()

