
def esqueleto(vertical, horizontal):
    # Criando uma lista dupla.
    skeleton = []
    tam, TAM = vertical, horizontal
    for i in range(tam):
        linhas = []
        for j in range(TAM):
            linhas.append(0)
        skeleton.append(linhas)
    return skeleton
def matriz(mat):
    # Só pra mostrar que o contéudo tá correto antes de printar.
    print(mat)
    #Pra passar pelos valores da lista.
    for x in range(len(mat)):
        # Printar o cabecário da Matriz
        if x == 0:
            print("   ", end="")
            for y in range(len(mat[x])):
                print(f" {y+1} |", end="")
        # Printar o "nome" da linha
        print(f"\n{x+1}: ", end="")
        # Printar as colunas
        for y in range(len(mat[x])):
            print(f" {mat[x][y]} |", end="")


def conversor(mat):
    index = []
    # Coletando as posições das ligações de uma mesma coluna em uma lista index
    for x in range(len(mat)):
        # Para poder auxiliar com o append ao temp.
        temp = []
        # Para o ponteiro não sair da lista
        # quando a quantia de vértices for maior que de arestas
        if x >= len(mat[x]):
            break
        # Quando a quantia de vértices for maior que de arestas.
        if len(mat) > len(mat[1]):
            for y in range(len(mat[x])):
                # Coletando os indíces caso encontre o número 1.
                if mat[y][x] == 1:
                    temp.append(y)
        # Quando a quantia de arestas for maior que dos vértices.
        else:
            for y in range(len(mat)):
                if mat[y][x] == 1:
                    temp.append(y)
        index.append(temp)
    # Criando a matriz de adjacência.
    adj = esqueleto(size_c, size_c)
    # Usando o pares de indíces armazenados em index,
    # Substituindo os zeros nas posições corretas pelas quantias de arestas.
    for x in range(len(index)):
        for y in range(len(index)):
            a = index[x][y]
            b = index[x][y+1]
            adj[a][b] += 1
            adj[b][a] += 1
            break
    matriz(adj)


def menu(mat):
    while(True):
        menu = input("\n1 - Ver Matriz\n2 - Alterar valores da Matriz\n3 - Converter em Matriz de Adjacência\n4 - Fechar programa\n- ").strip()
        if menu == "1":
            matriz(mat)
            print("\n")
        elif menu == "2":
            while(True):
                try:
                    linha = int(input("\nQual linha deve ser alterada?\n"))
                    col = int(input("\nE qual coluna deve ser alterada?\n"))
                    new = int(input("\nValor a ser colocado: \n"))
                    coluna[col - 1][linha - 1] = new
                    print("O valor foi alterado com sucesso !")
                    break
                except:
                    print("Utilize apenas valores cardinais.")
        elif menu == "3":
            conversor(mat)
        elif menu == "4":
            print("\nAdeus !")
            exit()
        elif menu == "0611":
            # Opção secreta para facilitar testes.
            mat[0][0] = 1
            mat[1][0] = 1
            mat[2][1] = 1
            mat[3][1] = 1
            mat[0][2] = 1
            mat[3][2] = 1
            mat[2][3] = 1
            mat[3][3] = 1
            print(mat)
        else:
            print("\nPor favor, insira um valor válido.")


while(True):
    try:
        size_c = int(input("Quantas vértices possui sua matriz?\n"))
        size_r = int(input("\nQuantas arestas possuia sua matriz?\n"))
    except:
        print("Tente novamente.")
    #size = 9
    coluna = esqueleto(size_c, size_r)
    print(coluna)
    menu(coluna)
    break
