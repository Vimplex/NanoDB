from Vertex import *

graph = GenesisVertex('test', '123', 123)

graph.add_collection(CollectionVertex(1, 'testing'))
graph.add_collection(CollectionVertex(2, 'users'))

graph.add_vertex(Vertex(1, CollectionVertex(1, 'testing'), {'user':'tester', 'timestamp':200}))
graph.add_vertex(Vertex(2, CollectionVertex(1, 'testing'), {'user':'peter', 'timestamp':320}))
graph.add_vertex(Vertex(3, CollectionVertex(2, 'users'), {'user':'user', 'timestamp':550}))

graph.show()