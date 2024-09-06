import networkx as nx
import matplotlib.pyplot as plt

# Matriz de adjacência fornecida
matriz_adjacencia = [
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]

# Criar grafo
G = nx.Graph()

# Adicionar nós e arestas ao grafo
for i in range(len(matriz_adjacencia)):
    G.add_node(i)
    for j in range(i+1, len(matriz_adjacencia[i])):
        if matriz_adjacencia[i][j] == 1:
            G.add_edge(i, j)

# Plotar o grafo
pos = nx.spring_layout(G)  # Define a posição dos nós
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.7)
plt.title("Grafo a partir da Matriz de Adjacência")
plt.show()
