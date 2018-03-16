#encoding= UTF-8
import os
from time import time
import random
from pyblake2 import blake2b
import unittest
from NanoDB import Graph 

class TestGraphDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestGraphDB.graph = Graph('testing', 'test')
    
    def test1_configCollection(self):
        TestGraphDB.graph.config_collection('123', unique=['user', 'timestamp'])

        result = self.graph.fast_query
        self.assertEqual(result['123']['unique'], ['user', 'timestamp'])
        
    
    def test2_addSingleNode(self):
        for _ in range(10):
            self.graph.add_single_node('123', {'user':random.randint(0, 100), 'timestamp': time(), 'species':'human'})
        self.graph.show_fastquery_data()


if __name__ == '__main__':
    unittest.main()