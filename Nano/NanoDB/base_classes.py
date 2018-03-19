
class Node:
    def __init__(self, properties):
        
        self.properties = properties

        self.edges = {}

    def add_edge(self, target_node, relation):
        if target_node not in self.edges or self.edges[target_node] != relation:
            self.edges[target_node] = relation
            return True
        
        else:
            print('edge already exists!')
            exit()

    def __str__(self):
        string = str(self.properties)
        if len(self.edges) > 0:
            string += '\nEdges:\n'
            for edge, relation in self.edges.items():
                string += str(edge)+', relation: '+str(relation)+ '\n'
        return string

    def __repr__(self):
        return self.__str__()

class Collection:
    def __init__(self, name):
        self.name = name
        
        self.cur_ID = 1
        self.nodes = {}

    def insert_node(self, node):
        
        self.nodes[self.cur_ID] = {'props':node.properties, 'edges':node.edges}
        self.cur_ID+=1
    
    def find_node(self, ID):
        try:
            return self.nodes[ID]
        except:
            print('Node does not exist')
    
    def __repr__(self):
        string = 'Collection: '+str(self.name)+'\n\n'
        if len(self.nodes) > 0:
            for ID, node in self.nodes.items():
                string += str(ID)+': '+str(node)+'\n'
        return string
    
    def __str__(self):
        return self.__repr__()