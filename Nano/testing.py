from NanoDB.base_classes import Node, Collection
import random
node1 = Node({'user':'Vincent', 'age':23, 'water':True})
node2 = Node({'user':'Vincent', 'age':23})


node1.add_edge(2, 5)
node1.add_edge(1, 4)
node2.add_edge(1, 4)


collection1 = Collection('testing')
collection1.insert_node(node1)
collection1.insert_node(node2)

collection2 = Collection('testing')
collection2.insert_node(node1)
collection2.insert_node(node2)

print(collection1)
print(collection2)

print(collection1.find_node({'water':True}))
