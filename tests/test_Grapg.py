import unittest
import random
from time import time
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from NanoDB import Graph
    else:
        from ..NanoDB import Graph

class Test_GraphDB(unittest.TestCase):


    @staticmethod
    def formatTime(t):
        if t < 1:
            return str(round(t*1000, 3)) + " ms"
        elif t >= 1 and t < 60:
            return str(round(t, 3))+ " sec"
        elif t >= 60:
            return str(int(t/60, 3)) + " min"

    @classmethod
    def setUpClass(cls):
        cls.start_time = time()
        cls.printer = []
        cls.pop = ['vince', 'test', 'ale', 'andres', 'Lorenz', 'Frida', 'Laura', 'Lea']
        
        cls.graph = Graph('test', 'testing')

    def setUp(self):
        print('\nstarting test')
        self.s_time = time()
    
    def test_1_insert(self):
        self.printer = 'test_insert'
        for collection in self.pop:
            for _ in range(50):
                self.graph.insert_node(collection, {'name': 'alex', 'age':random.randint(15, 50), 'time':time()})
        
    def test_2_find_nodes(self):
        result = []
        
        result += self.graph.find_node({'name':'alex'})
        for collection in result:
            self.assertEqual(collection.items()[0][1], [x for x in range(1, 51)])
            self.assertTrue(str(collection.keys()[0]) in self.pop)
    def tearDown(self):
        t_time = time()-self.s_time
        if len(self.printer) > 0:
            print('finished {0} in {1}'.format(str(self.printer), self.formatTime(t_time)))
        else:
            print('finished test in {0}'.format(self.formatTime(t_time)))
        self.printer = []

    @classmethod
    def tearDownClass(cls):
        print('\n'+str(cls.printer))
        print('\nThe test took '+str(cls.formatTime(time()-cls.start_time))+' to complete.')

if __name__ == '__main__':
    unittest.main()

