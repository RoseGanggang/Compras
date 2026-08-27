from banco import conectar


conexao = conectar()
cursor = conexao.cursor()


def adicionar_produto():
    print("\n" + "=" * 40)
    print("       ADICIONAR PRODUTO")
    print("=" * 40)

    nome = input("Nome do produto: ").strip()
    quantidade = int(input("Quantidade: "))

    cursor.execute("""
        INSERT INTO produtos (nome, quantidade)
        VALUES (%s, %s)
    """, (nome, quantidade))

    conexao.commit()

    print("\n" + "-" * 40)
    print("Produto adicionado com sucesso!")
    print(f"Produto: {nome}")
    print(f"Quantidade: {quantidade}")
    print("-" * 40)


def procurar_produto():
    print("\n" + "=" * 40)
    print("       PROCURAR PRODUTO")
    print("=" * 40)

    nome = input("Digite o nome do produto: ").strip()

    cursor.execute("""
        SELECT id, nome, quantidade
        FROM produtos
        WHERE nome ILIKE %s
        ORDER BY id
    """, (f"%{nome}%",))

    produtos = cursor.fetchall()

    if not produtos:
        print("\nProduto não encontrado.")
        return

    print("\n" + "-" * 55)
    print(f"{'ID':<6}{'PRODUTO':<35}{'QTD':>8}")
    print("-" * 55)

    for produto in produtos:
        id_produto, nome_produto, quantidade = produto

        print(f"{id_produto:<6}{nome_produto:<35}{quantidade:>8}")

    print("-" * 55)


def remover_produto():
    print("\n" + "=" * 40)
    print("        REMOVER PRODUTO")
    print("=" * 40)

    nome = input("Digite o nome do produto: ").strip()

    cursor.execute("""
        SELECT id, nome, quantidade
        FROM produtos
        WHERE nome ILIKE %s
        ORDER BY id
    """, (f"%{nome}%",))

    produtos = cursor.fetchall()

    if not produtos:
        print("\nProduto não encontrado.")
        return

    print("\nProdutos encontrados:")
    print("-" * 55)

    for produto in produtos:
        print(f"ID: {produto[0]} | Produto: {produto[1]} | Quantidade: {produto[2]}")

    print("-" * 55)

    try:
        id_produto = int(input("Digite o ID do produto que deseja remover: "))
    except ValueError:
        print("\nID inválido.")
        return

    cursor.execute("""
        SELECT nome, quantidade
        FROM produtos
        WHERE id = %s
    """, (id_produto,))

    produto = cursor.fetchone()

    if not produto:
        print("\nProduto não encontrado.")
        return

    confirmacao = input(
        f"Tem certeza que deseja remover '{produto[0]}'? (s/n): "
    ).strip().lower()

    if confirmacao != "s":
        print("\nOperação cancelada.")
        return

    cursor.execute("""
        DELETE FROM produtos
        WHERE id = %s
    """, (id_produto,))

    conexao.commit()

    print("\n" + "-" * 40)
    print("Produto removido com sucesso!")
    print(f"Produto: {produto[0]}")
    print("-" * 40)


def alterar_quantidade():
    print("\n" + "=" * 40)
    print("       ALTERAR QUANTIDADE")
    print("=" * 40)

    nome = input("Digite o nome do produto: ").strip()

    cursor.execute("""
        SELECT id, nome, quantidade
        FROM produtos
        WHERE nome ILIKE %s
        ORDER BY id
    """, (f"%{nome}%",))

    produtos = cursor.fetchall()

    if not produtos:
        print("\nProduto não encontrado.")
        return

    print("\nProdutos encontrados:")
    print("-" * 55)

    for produto in produtos:
        print(f"ID: {produto[0]} | Produto: {produto[1]} | Quantidade: {produto[2]}")

    print("-" * 55)

    try:
        id_produto = int(input("Digite o ID do produto: "))
        nova_quantidade = int(input("Digite a nova quantidade: "))

        if nova_quantidade < 0:
            print("\nA quantidade não pode ser negativa.")
            return

    except ValueError:
        print("\nDigite apenas números válidos.")
        return

    cursor.execute("""
        SELECT nome, quantidade
        FROM produtos
        WHERE id = %s
    """, (id_produto,))

    produto = cursor.fetchone()

    if not produto:
        print("\nProduto não encontrado.")
        return

    cursor.execute("""
        UPDATE produtos
        SET quantidade = %s
        WHERE id = %s
    """, (nova_quantidade, id_produto))

    conexao.commit()

    print("\n" + "-" * 40)
    print("Quantidade alterada com sucesso!")
    print(f"Produto: {produto[0]}")
    print(f"Quantidade anterior: {produto[1]}")
    print(f"Nova quantidade: {nova_quantidade}")
    print("-" * 40)