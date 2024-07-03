import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.listAnni = []

        self.graph = nx.Graph()
        self.nodes = []
        self.edges = []
        self.idMap = {}

        self.loadAnni()

    def loadAnni(self):
        self.listAnni = DAO.getAnni()

    def buildGraph(self, anno, giorni):
        self.graph.clear()
        self.nodes = DAO.getNodes()
        self.graph.add_nodes_from(self.nodes)
        for n in self.nodes:
            self.idMap[n.id] = n

        tmp = DAO.getEdges(anno, giorni, self.idMap)
        for e in tmp:
            self.edges.append(e)
            self.graph.add_edge(e[0], e[1], weight=e[2])

    def getGraphSize(self):
        return len(self.nodes), len(self.edges)

    def getAdiacenti(self):
        adiacenza = []
        for n in self.nodes:
            peso = 0
            for v in self.graph[n]:
                peso += self.graph[n][v]['weight']
            adiacenza.append((n, peso))
        return adiacenza
