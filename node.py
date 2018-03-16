from AVL.AVL_Tree import AVLTree


class Node:
    def __init__(self, collection, properties):
        self.collection = collection
        self.properties = properties
        self.relations = AVLTree()

        self.build()

    def build(self):
        return {self.collection:self.properties}