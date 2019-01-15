class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}

	def addNeighbour(self,nbr,weight=0):
		self.connectedTo[nbr]= weight

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]


class Graph:
	def __init__(self):
		self.vertlist={}
		self.numVertices=0

	def addVertex(self,key):
		self.numVertices=self.numVertices+1
		newVertex =  Vertex(key)
		self.vertlist[key]=newVertex
		return newVertex

	def getVertex(self,n):
		return n in self.vertlist

	def addEdge(self,f,t,cost=0):
		if f not in self.vertlist:
			nv = self.addVertex(f)
		if t not in self.vertlist:
			nv = self.addVertex(t)

		self.vertlist[f].addNeighbour(self.vertlist[t],cost)

	def getVertices(self):
		return self.vertlist.keys()

	def __iter__(self):
		return iter(self.vertlist.values())


g = Graph()
for i in range(6):
	g.addVertex(i)

g.addEdge(0,1,5)