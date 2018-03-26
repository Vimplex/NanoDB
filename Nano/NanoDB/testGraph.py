from Graph import Graph
from time import time

graph = Graph('test', 'test')
graph.insert_node('testing', {'user':'peter', 'time': time()})

print(graph)