def adicionar_livro(biblioteca, titulo, autor):
    for livro in biblioteca:
        if livro["titulo"] == titulo:
            print('O livro "' + titulo + '" já existe.')
            return
    biblioteca.append({"titulo": titulo, "autor": autor, "status": "disponível"})
    print('O livro "' + titulo + '" foi adicionado.')

def emprestar_livro(biblioteca, titulo):
    for livro in biblioteca:
        if livro["titulo"] == titulo:
            livro["status"] = "emprestado"
            print('O livro "' + titulo + '" foi emprestado.')
            return
    print('O livro "' + titulo + '" não foi encontrado.')

def devolver_livro(biblioteca, titulo):
    for livro in biblioteca:
        if livro["titulo"] == titulo:
            livro["status"] = "disponível"
            print('O livro "' + titulo + '" foi devolvido.')
            return
    print('O livro "' + titulo + '" não foi encontrado.')

def listar_livros(biblioteca):
    if biblioteca:
        for livro in biblioteca:
            print('Título: ' + livro["titulo"] + ', Autor: ' + livro["autor"] + ', Status: ' + livro["status"])
    else:
        print("Não há livros na biblioteca")

def main():
    biblioteca = []
    while True:
        print("Sistema de Gerenciamento de Biblioteca")
        print("1. Adicionar Livro")
        print("2. Emprestar Livro")
        print("3. Devolver Livro")
        print("4. Consultar Acervo")
        print("5. Sair do Sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            adicionar_livro(biblioteca, titulo, autor)
        elif opcao == "2":
            titulo = input("Digite o título do livro que deseja emprestar: ")
            emprestar_livro(biblioteca, titulo)
        elif opcao == "3":
            titulo = input("Digite o título do livro que será devolvido: ")
            devolver_livro(biblioteca, titulo)
        elif opcao == "4":
            listar_livros(biblioteca)
        elif opcao == "5":
            print("Saindo do sistema...")
            return
        else:
            print("Opção inválida, tente novamente.")
        print()

main()