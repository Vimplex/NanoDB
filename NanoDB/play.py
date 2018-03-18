from time import time
from Graph import Graph
from Vertex import *

test = Graph('test', '123')

col1 = CollectionVertex(1, 'testing')
col2 = CollectionVertex(2, 'users')

test.add_collection(col1)
test.add_collection(col2)

test.add_vertex(Vertex(1, col1, {'name':'vinc', 'timestamp':time()}))
test.add_vertex(Vertex(2, col1, {'name':'ginc', 'timestamp':time()}))
test.add_vertex(Vertex(3, col1, {'name':'tinc', 'timestamp':time()}))

test.add_vertex(Vertex(4, col2, {'name':'peter', 'timestamp':time()}))
test.add_vertex(Vertex(5, col2, {'name':'peter', 'timestamp':time()}))
test.add_vertex(Vertex(6, col2, {'name':'peter', 'timestamp':time()}))


test.show()