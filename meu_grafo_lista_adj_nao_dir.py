from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *
from collections import deque


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        conjunto_vertices = set()
        quant_vertices = len(self.vertices)

        for i in range(quant_vertices):
            for j in range(i + 1, quant_vertices):
                cond = 0
                for k in self.arestas:
                    if (self.arestas[k].v1.rotulo == self.vertices[i].rotulo) and (
                            self.arestas[k].v2.rotulo == self.vertices[j].rotulo):
                        cond = 1
                        break
                    if (self.arestas[k].v1.rotulo == self.vertices[j].rotulo) and (
                            self.arestas[k].v2.rotulo == self.vertices[i].rotulo):
                        cond = 1
                        break
                if (cond == 0):
                    conjunto_vertices.add(self.vertices[i].rotulo + '-' + self.vertices[j].rotulo)
        return conjunto_vertices

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.arestas:
            if self.arestas[i].v1 == self.arestas[i].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        cont = 0
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Não existe o vertice")
        for i in self.arestas:
            if self.arestas[i].v1.rotulo == V:
                cont += 1
            if self.arestas[i].v2.rotulo == V:
                cont += 1
        return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for a in self.arestas:
            for i in self.arestas:
                if a == i:
                    continue
                if ((self.arestas[a].v1 == self.arestas[i].v1 and self.arestas[a].v2 == self.arestas[i].v2) or (
                        self.arestas[a].v2 == self.arestas[i].v1 and self.arestas[a].v1 == self.arestas[i].v2)):
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista_aresta = set()
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Não existe o vertice")
        for i in self.arestas:
            if self.arestas[i].v1.rotulo == V:
                lista_aresta.add(i)
            if self.arestas[i].v2.rotulo == V:
                lista_aresta.add(i)
        return set(sorted(lista_aresta))

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        if (not (self.ha_paralelas() and self.ha_laco())):  # Se não houver laços ou paralelas
            qntVertices = len(self.vertices)
            for i in self.vertices:
                if (self.grau(i.rotulo) == qntVertices - 1):
                    continue
                else:
                    return False
            return True

        return False

    def dfs(self, V=''):
        arvore_dfs=MeuGrafo()
        arvore_dfs.adiciona_vertice(V)
        return self.dfs_rec(V,arvore_dfs)

    def dfs_rec(self, V, arvore_dfs):
        arestas= sorted(self.arestas_sobre_vertice(V))
        for i in arestas:
            if arvore_dfs.existe_rotulo_aresta(i):
                continue
            else:
               arestas2=self.get_aresta(i)
               if arestas2.v1.rotulo==V:
                   vertice_oposto= arestas2.v2.rotulo
               else:
                   vertice_oposto=arestas2.v1.rotulo
               if arvore_dfs.existe_rotulo_vertice(vertice_oposto):
                   continue
               else:
                   arvore_dfs.adiciona_vertice(vertice_oposto)
                   arvore_dfs.adiciona_aresta(arestas2)
                   self.dfs_rec(vertice_oposto,arvore_dfs)
        return arvore_dfs


    def bfs(self, V=''):
        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(V)
        return self.rec(V, arvore_bfs)


    def rec(self,V,arvore_bfs):
        lista_vertices = []
        arestas = sorted(self.arestas_sobre_vertice(V))
        for i in arestas:
            if arvore_bfs.existe_rotulo_aresta(i):
                continue
            else:
                arestas2 = self.get_aresta(i)
                if arestas2.v1.rotulo == V:
                    vertice_oposto = arestas2.v2.rotulo
                else:
                    vertice_oposto = arestas2.v1.rotulo
                if arvore_bfs.existe_rotulo_vertice(vertice_oposto):
                    continue
                else:
                    arvore_bfs.adiciona_vertice(vertice_oposto)
                    arvore_bfs.adiciona_aresta(arestas2)
                    lista_vertices.append(vertice_oposto)
        for i in lista_vertices:
            self.rec(i,arvore_bfs)

        return arvore_bfs

    def ha_ciclo():
        





