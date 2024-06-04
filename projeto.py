def adicionar_livro(biblioteca, titulo, autor):
    if titulo not in biblioteca:
        biblioteca[titulo] = {"autor": autor, "status": "disponível"}
        print(f'O livro "{titulo}" foi adicionado.')
    else:
        print(f'O livro "{titulo}" já existe na biblioteca.')

def emprestar_livro(biblioteca, titulo):
   if titulo in biblioteca:
       del biblioteca[titulo]
       print (f'O livro "{titulo}" foi emprestado.')
   else:
       print(f'O livro "{titulo}" não encontrado na biblioteca.')

def devolver_livro(biblioteca, titulo):
    if titulo in biblioteca:
        del biblioteca[titulo]
        print (f'O livro "{titulo}" foi devolvido.')
    else:
        print(f'O livro "{titulo}" não encontrado na biblioteca.')

def listar_livros(biblioteca):
    if biblioteca:
        for titulo, dados in biblioteca.items():
             print(f'Título: {titulo}, Autor: {dados["autor"]}, Status: {dados["status"]}')
    else:
      print("A biblioteca está vazia.")

def main():
    biblioteca = {}
    while True:
        print("\nSistema de Gerenciamento de Biblioteca")
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
            titulo = input("Digite o título do livro a ser empretado: ")
            emprestar_livro(biblioteca, titulo)
        elif opcao == "3":
            titulo = input("Digite o título do livro a ser devolvido: ")
            devolver_livro(biblioteca, titulo)
        elif opcao == "4":
            listar_livros(biblioteca)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()