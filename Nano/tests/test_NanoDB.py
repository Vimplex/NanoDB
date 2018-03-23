import unittest
import random
from time import time
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from NanoDB import base_classes
    else:
        from ..NanoDB import base_classes

class Test_GraphDB_base_classes(unittest.TestCase):


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
        
        cls.col1 = base_classes.Collection('col1')
        cls.col2 = base_classes.Collection('col2')
        cls.col3 = base_classes.Collection('col3')
        for _ in range(100):
            node1 = base_classes.Node({'user':random.sample(cls.pop, 1)[0], 'age':random.randint(15, 50)})
            cls.col1.insert_node(node1)
            node2 = base_classes.Node({'user':random.sample(cls.pop, 1)[0], 'age':random.randint(15, 50)})
            cls.col2.insert_node(node2)
            node3 = base_classes.Node({'user':random.sample(cls.pop, 1)[0], 'age':random.randint(15, 50)})
            cls.col3.insert_node(node3)
        
    def test_col_creation(self):
        result1 = self.col1.get_collection_size()
        result2 = self.col2.get_collection_size()
        result3 = self.col3.get_collection_size()
        self.assertEqual(result1, 100)
        self.assertEqual(result2, 100)
        self.assertEqual(result3, 100)

        counter = {'len':[0, 0, 0], 'val':[{}, {}, {}]}
        for user in self.pop:
            result1 = self.col1.find_node({'user':user})
            result2 = self.col2.find_node({'user':user})
            result3 = self.col3.find_node({'user':user})

            counter['len'][0] += len(result1)
            counter['len'][1] += len(result2)
            counter['len'][2] += len(result3)

            counter['val'][0][user] = len(result1)
            counter['val'][1][user] = len(result2)
            counter['val'][2][user] = len(result3)

        self.assertEqual(counter['len'], [100, 100, 100], msg='All collections have 100 elements')
        Test_GraphDB_base_classes.printer.append(counter['val'])

    
    @classmethod
    def tearDownClass(cls):
        print('\n'+str(cls.printer))
        print('\nThe test took '+str(cls.formatTime(time()-cls.start_time))+' to complete.')
if __name__ == '__main__':
    unittest.main()
