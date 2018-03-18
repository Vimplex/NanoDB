class Node:
	def __init__(self,index=None):
		self.index=index
		self.left_child=None
		self.right_child=None
		self.parent=None # pointer to parent node in tree
		self.height=1 # height of node in tree (max dist. to leaf) NEW FOR AVL
