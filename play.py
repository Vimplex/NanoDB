from graph import Graph

graph = Graph('test')
graph.config_collection('testing', unique=['user'])
graph.add_single_node('testing', {'user':'Vincent', 'timestamp':12345})
graph.add_single_node('testing', {'user':'Vincent', 'timestamp':12345})
graph.show_fastquery_data()