from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from meu_grafo_lista_adj_nao_dir import MeuGrafo

g_4_bfs = MeuGrafo()
g_4_bfs.adiciona_vertice("A")
g_4_bfs.adiciona_vertice("B")
g_4_bfs.adiciona_vertice("C")
g_4_bfs.adiciona_vertice("D")
g_4_bfs.adiciona_aresta("a1", "A", "B")
g_4_bfs.adiciona_aresta("a3", "A", "D")
g_4_bfs.adiciona_aresta("a2", "B", "C")

"""""
grafoteste.adiciona_vertice("A")
grafoteste.adiciona_vertice("E")
grafoteste.adiciona_vertice("I")
grafoteste.adiciona_vertice("C")
grafoteste.adiciona_vertice("K")
grafoteste.adiciona_vertice("J")

grafoteste.adiciona_aresta('a1','A','E')
grafoteste.adiciona_aresta('a2','E','I')
grafoteste.adiciona_aresta('a3','I','C')
grafoteste.adiciona_aresta('a4','K','C')
grafoteste.adiciona_aresta('a5','C','J')"""

print("GRAFO SEM AS FUNÇÕES")
print(g_4_bfs)
#print("Função DFS")
#print(g_7_dfs.dfs("C"))
print("Função BFS")
print(g_4_bfs.bfs("B"))


