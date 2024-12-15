from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        vna= set()
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if len(self.matriz[i][j]) == 0 and i<j:
                    vna.add("{}-{}".format(self.vertices[i].rotulo, self.vertices[j].rotulo))
        return vna


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.matriz)):
            if len(self.matriz[i][i])>0:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError( "O vértice não existe no grafo")

        grau=0
        vertice=self.get_vertice(V)
        index=self.indice_do_vertice(vertice)

        for i in range(len(self.vertices)):
           if i==index:
               grau+=2 * len(self.matriz[index][i])
           else:
               grau+=len(self.matriz[index][i])

        return grau




    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if len(self.matriz[i][j]) >1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        asv=set()
        vert=[]
        cont=0

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError( "O vértice não existe no grafo")

        for i in range(len(self.matriz)):
            vert.append(self.vertices[i].rotulo)

        for a in range(len(vert)):
            if vert[a]==V:
                cont+=a

        for j in range(len(self.matriz)):
            dic= self.matriz[cont][j]
            for c in dic.keys():
                asv.add(c)
        return asv


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        # Verificar se há laços ou arestas paralelas
        if self.ha_laco() or self.ha_paralelas():
            return False
        else:
            if self.vertices_nao_adjacentes() == set():
                    return True
            return False

