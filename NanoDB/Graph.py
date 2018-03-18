from time import time
import os

from pyblake2 import blake2b

from Vertex import *

class Graph:
    def __init__(self, name, password):
        self.graph_name = name
        try:
            self.password = blake2b(password.encode()).hexdigest()
        except:
            self.password = password
        self.timestamp = time()

        self.root = GenesisVertex(self.graph_name, self.password, self.timestamp)

    def add_collection(self, collection_vertex):
        if collection_vertex.ID not in self.root.collections:
            self.root.collections[collection_vertex.ID] = {}
            return True
        else:
            print('colletion already initialized!')
            return False
    
    def add_vertex(self, vertex):
        if vertex.collection.ID in self.root.collections:
            self.root.collections[vertex.collection.ID][vertex.ID] = vertex.properties
        else:
            print(self.root.collections)
            print('The given collection does not exists, please initialize the collection first!')
            return False
    
    def show(self):
        for key, value in self.root.collections.items():
            print(str(key)+'\n')
            for v_id, v_pro in value.items():
                print(str(v_id)+' :'+str(v_pro))
            print('\n')