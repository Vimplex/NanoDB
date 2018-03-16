import os

from pyblake2 import blake2b

from AVL.AVL_Tree import AVLTree
from node import Node

class Graph:
    def __init__(self, Name, Password=None):
        self.Name = Name
        if Password != None:
            self.Password = self.password = blake2b(Password.encode()).hexdigest()
        else:
            self.Password = Password
        
        # initializing main attributes

        # determine paths
        base_path = os.path.dirname(__file__)
        self.data_path = os.path.join(base_path, 'data')
        self.hdf5_path = os.path.join(self.data_path, 'hdf5')
        self.nano_path = os.path.join(self.data_path, 'nano')

        # defining main data-holding attributes

        self.nodes_to_add = []
        self.nodes_to_update = []

        self.fast_query = {}

        self.fast_query_data = {}

        # initialize main counters and managers

        self.cur_index = 1

    def config_collection(self, collection, **configs):
        possible_configs = ['unique']
        # if fast_query
        if collection not in self.fast_query: # add collection to fast_queries, with given parameters
            configs_to_add = {}
            for key, value in configs.items():
                # check if key is valid
                if key not in possible_configs:
                    continue
                
                if key == 'unique':
                    # check if 'unique' is a list
                    if type(value) != list:
                        print('no list!')
                        continue
                    else:
                        unique_columns = []
                        for column in value:
                            # check if column name is of valid data-type
                            if type(column) != str and type(column) != int and type(column) != float:
                                print('type error')
                                continue
                            else:
                                unique_columns.append(column)
                        configs_to_add[key] = unique_columns
                        
                else:
                    configs_to_add[key] = value
                    
            self.fast_query[collection] = configs_to_add
        else:# update properties in fast_query collection
            configs_to_update = {}
            for key, value in configs.items():
                # check if key valid
                if key not in possible_configs:
                    continue
                
                if key == 'unique':
                    print('unique')
                    if type(value) != list:
                        print('no list!')
                        continue
                    else:
                        unique_columns = []
                        for column in value:
                            if type(column) != str and type(column) != int and type(column) != float:
                                print('type error')
                                continue
                            else:
                                unique_columns.append(column)
                        configs_to_add[key] = unique_columns
                        
                else:
                    configs_to_add[key] = value
                    
            for key, config in configs_to_update.items():
                if key in self.fast_query[collection]:
                    if self.fast_query[collection][key] == config:
                        continue    
                self.fast_query[collection][key] = config

    def add_single_node(self, collection, properties):
        index = self.cur_index
        self.cur_index += 1
        if collection in self.fast_query:
            
            for properti, value in properties.items():
                if properti in self.fast_query[collection]['unique']:
                    if collection not in self.fast_query_data:
                        self.fast_query_data[collection] = {}
                    if properti not in self.fast_query_data[collection]:
                        self.fast_query_data[collection][properti] = [value]
                    elif value not in self.fast_query_data[collection][properti]:
                        self.fast_query_data[collection][properti].append(value)
                else:
                    if collection not in self.fast_query_data:
                        self.fast_query_data[collection] = {}
                    if properti not in self.fast_query_data[collection]:
                        self.fast_query_data[collection][properti] = {}
                    if value not in self.fast_query_data[collection][properti]:
                        self.fast_query_data[collection][properti][value] = AVLTree()
                    self.fast_query_data[collection][properti][value].insert(index)

       
    def show_fastquery_data(self):
        print(self.fast_query_data)
