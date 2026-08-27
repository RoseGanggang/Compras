import os
import inquirer

from mostrar import mostrar_produtos
from produtos import (
    adicionar_produto,
    procurar_produto,
    alterar_quantidade,
    remover_produto
)


def limpar_tela():
    os.system("clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def titulo(texto):

    print("\n")
    print("=" * 60)
    print(f"{texto:^60}")
    print("=" * 60)


def menu_produtos():

    while True:

        limpar_tela()

        titulo("GERENCIAR PRODUTOS")

        perguntas = [
            inquirer.List(
                "opcao",
                message="Escolha uma opção",
                choices=[
                    "Ver produtos",
                    "Procurar produto",
                    "Adicionar produto",
                    "Alterar quantidade",
                    "Remover produto",
                    "Voltar"
                ]
            )
        ]

        resposta = inquirer.prompt(perguntas)

        if resposta is None:
            return

        opcao = resposta["opcao"]

        # ==========================================
        # VER PRODUTOS
        # ==========================================

        if opcao == "Ver produtos":

            limpar_tela()

            titulo("LISTA DE PRODUTOS")

            mostrar_produtos()

            pausar()

        # ==========================================
        # PROCURAR PRODUTO
        # ==========================================

        elif opcao == "Procurar produto":

            limpar_tela()

            titulo("PROCURAR PRODUTO")

            procurar_produto()

            pausar()

        # ==========================================
        # ADICIONAR PRODUTO
        # ==========================================

        elif opcao == "Adicionar produto":

            limpar_tela()

            titulo("ADICIONAR PRODUTO")

            adicionar_produto()

            pausar()

        # ==========================================
        # ALTERAR QUANTIDADE
        # ==========================================

        elif opcao == "Alterar quantidade":

            limpar_tela()

            titulo("ALTERAR QUANTIDADE")

            alterar_quantidade()

            pausar()

        # ==========================================
        # REMOVER PRODUTO
        # ==========================================

        elif opcao == "Remover produto":

            limpar_tela()

            titulo("REMOVER PRODUTO")

            remover_produto()

            pausar()

        # ==========================================
        # VOLTAR
        # ==========================================

        elif opcao == "Voltar":

            return


def menu_principal():

    while True:

        limpar_tela()

        titulo("LISTA DE COMPRAS")

        perguntas = [
            inquirer.List(
                "opcao",
                message="MENU PRINCIPAL",
                choices=[
                    "Gerenciar produtos",
                    "Sair"
                ]
            )
        ]

        resposta = inquirer.prompt(perguntas)

        if resposta is None:
            break

        opcao = resposta["opcao"]

        # ==========================================
        # GERENCIAR PRODUTOS
        # ==========================================

        if opcao == "Gerenciar produtos":

            menu_produtos()

        # ==========================================
        # SAIR
        # ==========================================

        elif opcao == "Sair":

            limpar_tela()

            titulo("LISTA DE COMPRAS")

            print("\nObrigado por utilizar o sistema!")

            print("\nEncerrando...")

            break


if __name__ == "__main__":
    menu_principal()