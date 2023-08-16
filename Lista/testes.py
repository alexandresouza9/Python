produtos = ["feijão","arroz","açúcar","macarrão","sal"]

def visualizarProdutos(arr):
  for i in range(len(arr)):
    posicao = i
    produto = arr[i]
    print(f"Produto na posição {posicao}: {produto}" )
def alterarProduto(produto_antigo, produto_novo, arr):
  achou = False

  for i in range(len(arr)):
    if arr[i] == produto_antigo:
      arr[i] = produto_novo
      achou = True
      break

  if achou == False:
    print("Produto não cadastrado!")
  else:
    print(f"O produto {produto_antigo}, foi substituído por {produto_novo}")

def adicionarProduto(produto_cadastro, arr):
  produtos.append(produto_cadastro)
  print(f"Produto {produto_cadastro} foi adicionado")

while(True):
    #Monta menu
    menu = int(input("""******* SISTEMA DA LOJA *******
Selecione a versão do sistema:
1 - Visualizar Lista de Produtos
2 - Alterar Produto
3 - Adicionar Produto
0 - Sair
"""))

    #verifica a entrada e executa a opção
    if menu < 0:
        print("Entrada inválida.")
    elif menu == 1:
        visualizarProdutos(produtos)
        break
    elif menu == 2:
        produtoAntigo = input("Digite o nome do produto a ser substituído: ")
        produtoNovo = input("Digite o nome do produto novo: ")
        alterarProduto(produtoAntigo, produtoNovo, produtos)
        break
    elif menu == 3:
        produtoCadastro = input("Digite o nome do produto a ser cadastrado: ")
        adicionarProduto(produtoCadastro,produtos)
        break
    elif menu == 0:
      break
    else:
      print("Entrada inválida.")

    print("*" * 42)

