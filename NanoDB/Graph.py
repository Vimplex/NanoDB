from base_classes import *
from pyblake2 import blake2b

class Graph:
    def __init__(self, Name, Password):
        self.Name = Name
        if Password is not None:
            self.Password = blake2b(str(Password).encode())
        else:
            self.Password = Password
        
        self.collections = {}
        
    def insert_node(self, collection, properties):
        if collection not in self.collections:
            self.collections[collection] = Collection(collection)

        node = Node(properties)
        self.collections[collection].insert_node(node)
    def find_node(self, properties, collections=[]):
        to_return = []
        if len(collections)> 0:
            for collection in collections:
                if collection in self.collections:
                   
                    result = self.collections[collection].find_node(properties)
                    if len(result) == 0:
                        continue
                    else:
                        to_return + result
        else:
            for name, collection in self.collections.items():
                result = collection.find_node(properties)
                if len(result) == 0:
                    continue
                else:
                    to_return.append({name:result})
        
        return to_return
    
    def __repr__(self):
        string = ''
        if len(self.collections) > 0:
            for _, collection in self.collections.items():
                string += ('\n'+collection.name+'\n')
                for propertie, ID in collection.nodes.items():
                    string += propertie+': '+str(ID)+'\n'
        return string
                

                    
    
                

        
        
