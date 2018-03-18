from pyblake2 import blake2b


class Vertex:
    def __init__(self, ID, collection, properties):
        self.ID = ID
        self.collection = collection
        self.properties = properties
        self.edges = {}

    def add_edge(self,target_vertex_id, relation):
        if target_vertex_id not in self.edges:
            self.edges[target_vertex_id] = relation
            return True
        else:
            print('A relation to the given vertex already exists. You can only create one relation from one vertex to any other vertex.')
            return False


    def __repr__(self):
        return "{}".format({self.collection:{self.ID:self.properties}})

    def __str__(self):
        return self.__repr__()

class GenesisVertex:
    def __init__(self, graph_name, password, timestamp):
        self.graph_name = graph_name      
        self.password = password
        self.timestamp = timestamp

        self.collections = {}

  
class CollectionVertex:
    def __init__(self, ID, collection_name):
        self.ID = ID
        self.collection_name = collection_name

        self.vertices = {}

    