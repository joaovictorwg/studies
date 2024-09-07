import os

import matplotlib.pyplot as plt
import networkx as nx

# Função hierarchy_pos agora está fora da classe Grafo
def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    return pos

def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)  
    
    if len(children) != 0:
        dx = width / 2 
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
        
    return pos

class Grafo:
    #iniciar a matriz
    def __init__(self, matriz_adjacencia):
        self.matriz_adjacencia = matriz_adjacencia
        self.num_vertices = len(matriz_adjacencia)
        self.visitado = [False] * self.num_vertices
        self.cor = [None] * self.num_vertices
        self.componentes_conexas = []

    #busca em largura
    def bfs(self, raiz):
        fila = []
        fila.append(raiz)
        self.visitado[raiz] = True
        componente = [raiz]

        while fila:
            v = fila.pop(0)
            for u in range(self.num_vertices):
                if self.matriz_adjacencia[v][u] == 1 and not self.visitado[u]:
                    fila.append(u)
                    self.visitado[u] = True
                    componente.append(u)
                    self.cor[u] = not self.cor[v]  # Alternar a cor para bipartição

        self.componentes_conexas.append(componente)


    #armazenar arvore para ser plotada
    def bfs_com_arvore(self, raiz):
        
        fila = [raiz]
        visitados_bfs = [False] * self.num_vertices
        arvore_bfs = {v: [] for v in range(self.num_vertices)}

        indice_frente = 0  # Índice do início da fila
        while indice_frente < len(fila):
            v = fila[indice_frente]
            indice_frente += 1

            if not visitados_bfs[v]:
                for u in range(self.num_vertices):
                    if self.matriz_adjacencia[v][u] == 1 and not visitados_bfs[u]:
                        fila.append(u)
                        visitados_bfs[u] = True
                        arvore_bfs[v].append(u)

        return arvore_bfs

    

    #plotar arvore
    def visualizar_arvore_bfs(self, raiz, arvore_bfs):
        G = nx.Graph()

        for u, vizinhos in arvore_bfs.items():
            G.add_node(u)
            for v in vizinhos:
                G.add_edge(u, v)

        pos = hierarchy_pos(G, raiz)  # Utilize o layout hierarchical_pos
        cores = ['red' if self.cor[i] else 'blue' for i in range(self.num_vertices)]

        # Certifique-se de que todos os nós na árvore tenham posição definida
        for node in G.nodes:
            if node not in pos:
                pos[node] = (0, 0)

        nx.draw(G, pos, node_color=cores, with_labels=True, font_color='white')
        plt.title(f"Árvore de Busca em Largura a partir do vértice {raiz}")
        plt.show()

    

    #verificar se é um grafo conexo
    def verificar_conexo(self):
        return len(self.componentes_conexas) == 1

    #encontrar a bipartição se for bipartido
    def encontrar_biparticao(self):
        for v in range(self.num_vertices):
            if not self.visitado[v]:
                self.bfs(v)

        # Verificar se o grafo é bipartido
        bipartido = all(self.cor[u] != self.cor[v] for u in range(self.num_vertices) for v in range(self.num_vertices) if self.matriz_adjacencia[u][v] == 1)

        if bipartido:
            print("\nO grafo é bipartido")
            self.mostrar_biparticao()
            
        else:
            print("\nO grafo não é bipartido.")
            ciclo_impar = self.encontrar_ciclo_impar(0)
            if ciclo_impar:
                print(f"O grafo possui um ciclo ímpar: {ciclo_impar[0]} e {ciclo_impar[1]}")
            else:
                print("O grafo não possui ciclo ímpar.")


    #encontrar a biparticao com arvore
    def encontrar_biparticao_com_arvore(self, raiz):
        arvore_bfs = self.bfs_com_arvore(raiz)
        fila = []
        fila.append(raiz)
        visitados_bfs = [False] * self.num_vertices
        candidatos = [v for v in range(self.num_vertices) if self.matriz_adjacencia[raiz][v] == 1]

        print(f"Candidatos disponíveis para a escolha: {candidatos}")

        indice_frente = 0  # Índice do início da fila
        indice_final = 1   # Índice do final da fila

        while indice_frente < indice_final:
            v = fila[indice_frente]
            indice_frente += 1

            if not visitados_bfs[v]:
                print(f"Visitando vértice {v}")
                visitados_bfs[v] = True
                for u in arvore_bfs[v]:
                    fila.append(u)
                    indice_final += 1
                candidatos = [v for v in candidatos if v != raiz and not visitados_bfs[v]]
                print(f"Candidatos restantes: {candidatos}")
                if not candidatos:
                    print(f"\nO grafo não é mais bipartido a partir do vértice {v}\n")
                    break


    #mostrar a bipartição
    def mostrar_biparticao(self):
        if self.verificar_conexo():
            print("\nO grafo é conexo.\n")
            print("Bipartição:")
            for i in range(self.num_vertices):
                print(f"Vértice {i}: Grupo {'A' if self.cor[i] else 'B'}")
        else:
            print("O grafo não é conexo.")
            for i, componente in enumerate(self.componentes_conexas):
                print(f"Componente Conexa {i + 1}: {componente}")

    #mostrar a busca em largura
    def mostrar_bfs(self, raiz, arvore_bfs, cor=None):
        print("Busca em Largura:")
        fila = []
        fila.append(raiz)
        visitados_bfs = [False] * self.num_vertices
        indice_frente = 0  # Índice do início da fila

        while indice_frente < len(fila):
            v = fila[indice_frente]
            indice_frente += 1

            if not visitados_bfs[v]:
                print(f"Visitando vértice {v}")
                visitados_bfs[v] = True
                for u in arvore_bfs[v]:
                    fila.append(u)

        if cor is not None:
            cores = ['red' if cor[i] else 'blue' for i in range(self.num_vertices)]
        else:
            cores = 'blue'

        G = nx.Graph()

        for i in range(self.num_vertices):
            G.add_node(i)

        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.matriz_adjacencia[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.spring_layout(G)

        nx.draw(G, pos, node_color=cores, with_labels=True, font_color='white')
        plt.title(f"Árvore de Busca em Largura a partir do vértice {raiz}")
        plt.show()

    #listagem dos vertices candidatos
    def mostrar_bfs_com_candidatos(self, raiz):
        print("Busca em Largura:")
        fila = []
        fila.append(raiz)
        visitados_bfs = [False] * self.num_vertices
        candidatos = [v for v in range(self.num_vertices) if self.matriz_adjacencia[raiz][v] == 1]

        print(f"Candidatos disponíveis para a escolha: {candidatos}")

        while fila:
            v = fila.pop(0)
            if not visitados_bfs[v]:
                print(f"Visitando vértice {v}")
                visitados_bfs[v] = True
                for u in range(self.num_vertices):
                    if self.matriz_adjacencia[v][u] == 1 and not visitados_bfs[u]:
                        fila.append(u)
                candidatos = [v for v in candidatos if v != raiz and not visitados_bfs[v]]
                print(f"Candidatos restantes: {candidatos}")


    #encontrar ciclo impar se não for bipartido
    def encontrar_ciclo_impar(self, raiz):
        fila = []
        fila.append(raiz)
        nivel = [float('inf')] * self.num_vertices
        nivel[raiz] = 0
        indice_frente = 0 

        while indice_frente < len(fila):
            v = fila[indice_frente]
            indice_frente += 1

            for u in range(self.num_vertices):
                if self.matriz_adjacencia[v][u] == 1:
                    if nivel[u] == float('inf'):
                        nivel[u] = nivel[v] + 1
                        fila.append(u)
                    elif nivel[v] % 2 == nivel[u] % 2:
                        return (nivel[v], nivel[u])

        return None

    #plotar o grafo
    def visualizar_grafo(self):
        G = nx.Graph()

        for i in range(self.num_vertices):
            G.add_node(i)

        for i in range(self.num_vertices):
            for j in range(i+1, self.num_vertices):
                if self.matriz_adjacencia[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.spring_layout(G)
        cores = ['red' if self.cor[i] else 'blue' for i in range(self.num_vertices)]

        nx.draw(G, pos, node_color=cores, with_labels=True)
        plt.show()

# ler o arquivo "grafo.txt" e criar a matriz de adjacência
def ler_matriz_adjacencia(arquivo):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.read().splitlines()
            matrizes_adjacencia = []
            matriz_atual = []

            for linha in linhas:
                if not linha.strip():  # Linha em branco indica o fim de uma matriz
                    if matriz_atual:  # Adicionar a matriz apenas se ela não for vazia
                        matrizes_adjacencia.append(matriz_atual)
                        matriz_atual = []
                else:
                    matriz_atual.append(list(map(int, linha.split())))

            if matriz_atual:  # Adicionar a última matriz se houver uma linha em branco no final
                matrizes_adjacencia.append(matriz_atual)

        return matrizes_adjacencia

    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado. Verifique o caminho do arquivo.")
        return []

# imprimir a matriz de adjacência
def imprimir_matriz_adjacencia(matriz_adjacencia):
    for i in range(len(matriz_adjacencia)):
        print(matriz_adjacencia[i])

# main com opções para o usuario
if __name__ == "__main__":
    nome_arquivo = "grafo.txt"
    matrizes_adjacencia = ler_matriz_adjacencia(nome_arquivo)
    

    print(f"Foram carregadas {len(matrizes_adjacencia)} matriz(es) de adjacência.")
    indice_matriz = int(input("Qual matriz deseja utilizar? (Digite o índice inicando por 0): "))

    grafo = Grafo(matrizes_adjacencia[indice_matriz])
    
    imprimir_matriz_adjacencia(grafo.matriz_adjacencia)
    grafo.visualizar_grafo()

    for v in range(grafo.num_vertices):
        if not grafo.visitado[v]:
            grafo.bfs(v)
    
    while True:
        print("==============================================")
        print("Opções:")
        print("1 - Verificar se o grafo é conexo")
        print("2 - Aplicar Busca em Largura")
        print("3 - Encontrar Bipartição")
        print("0 - Sair do programa")

        opcao = input("Digite a Opção Desejada: ")

        if opcao == '0':
            print("Programa Encerrado!")
            break
        elif opcao == '1':
            if grafo.verificar_conexo():
                print("O grafo é conexo.")
                for i, componente in enumerate(grafo.componentes_conexas):
                    print(f"Componente Conexa {i + 1}: {componente}")
                    grafo.visualizar_grafo()
            else:
                print("O grafo não é conexo.")
                grafo.visualizar_grafo()
        elif opcao == '2':
            candidatos_raiz = [v for v in range(grafo.num_vertices) if not grafo.visitado[v]]
            print(f"Vértices disponíveis para escolha do vértice raiz: {candidatos_raiz}\n")
            raiz_bfs = int(input("Qual será o vértice raiz da busca? \n"))
            arvore_bfs = grafo.bfs_com_arvore(raiz_bfs)
            grafo.visualizar_arvore_bfs(raiz_bfs, arvore_bfs)
            grafo.encontrar_biparticao_com_arvore(raiz_bfs)
        elif opcao == '3':
            grafo.encontrar_biparticao()
            grafo.visualizar_grafo()
        else:
            print("Opção inválida. Tente novamente.")