
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
        for key, propertie in node.properties.items():
            if key not in self.nodes:
                self.nodes[key] = {propertie:[self.cur_ID]}
            elif propertie not in self.nodes[key]:
                self.nodes[key][propertie] = [self.cur_ID]
            else:
                self.nodes[key][propertie].append(self.cur_ID)
        self.cur_ID+=1
    
    def find_node(self, properties):
        nodes_to_return = set()
        nodes_with_props = []
       
        if len(properties) > 1:
            for key, propertie in properties.items():
                
                if key in self.nodes:
                    if propertie in self.nodes[key]:
                        if len(nodes_with_props) >0:
                            checked_Ids = []
                            for ID in self.nodes[key][propertie]:
                                if ID in nodes_with_props:
                                    checked_Ids.append(ID)
                                else:
                                    continue
                            nodes_with_props = checked_Ids
                        else:
                            nodes_with_props = self.nodes[key][propertie]
            
            nodes_to_return = set(nodes_with_props)

        elif len(properties) ==1:
            for key, propertie in properties.items():
                if key in self.nodes:
                    if propertie in self.nodes[key]:
                        nodes_to_return = self.nodes[key][propertie]

        return nodes_to_return
    
    def get_collection_size(self):
        return self.cur_ID-1

    def __repr__(self):
        return str(self.__class__)+'("'+self.name+'") '+str(self.cur_ID-1)+' entries'
    
    def __str__(self):
        string = 'Collection: '+str(self.name)+'\n\n'
        if len(self.nodes) > 0:
            for ID, node in self.nodes.items():
                string += str(ID)+': '+str(node)+'\n'
        return string
    