from AVL_node import Node

class AVLTree:
	def __init__(self):
		self.root=None
    
	def insert(self,index):
		if self.root==None:
			self.root=Node(index)
		else:
			self.__insert(index,self.root)

	def __insert(self,index,cur_node):
		if index<cur_node.index:
			if cur_node.left_child==None:
				cur_node.left_child=Node(index)
				cur_node.left_child.parent=cur_node # set parent
				self.__inspect_insertion(cur_node.left_child)
			else:
				self.__insert(index,cur_node.left_child)
		elif index>cur_node.index:
			if cur_node.right_child==None:
				cur_node.right_child=Node(index)
				cur_node.right_child.parent=cur_node # set parent
				self.__inspect_insertion(cur_node.right_child)
			else:
				self.__insert(index,cur_node.right_child)
		else:
			print("index already in tree!")

	def traverse_in_order(self):
		if self.root!=None:
			self.__traverse_in_order(self.root)

	def __traverse_in_order(self,cur_node):
		if cur_node!=None:
			self.__traverse_in_order(cur_node.left_child)
			print ('%s, h=%d'%(str(cur_node.index),cur_node.height))
			self.__traverse_in_order(cur_node.right_child)

	def height(self):
		if self.root!=None:
			return self.__height(self.root,0)
		else:
			return 0

	def __height(self,cur_node,cur_height):
		if cur_node==None: return cur_height
		left_height=self.__height(cur_node.left_child,cur_height+1)
		right_height=self.__height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)

	def find(self,index):
		if self.root!=None:
			return self.__find(index,self.root)
		else:
			return None

	def __find(self,index,cur_node):
		if index==cur_node.index:
			return cur_node
		elif index<cur_node.index and cur_node.left_child!=None:
			return self.__find(index,cur_node.left_child)
		elif index>cur_node.index and cur_node.right_child!=None:
			return self.__find(index,cur_node.right_child)

	def delete_index(self,index):
		return self.delete_node(self.find(index))

	def delete_node(self,Node):

		# Protect against deleting a Node not found in the tree
		if Node==None or self.find(Node.index)==None:
			print("Node to be deleted not found in the tree!")
			return None 

		# returns the Node with min index in tree rooted at input Node
		def min_index_node(n):
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		# returns the number of children for the specified Node
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children

		# get the parent of the Node to be deleted
		node_parent=Node.parent

		# get the number of children of the Node to be deleted
		node_children=num_children(Node)

		# break operation into different cases based on the
		# structure of the tree & Node to be deleted

		# CASE 1 (Node has no children)
		if node_children==0:

			if node_parent!=None:
				# remove reference to the Node from the parent
				if node_parent.left_child==Node:
					node_parent.left_child=None
				else:
					node_parent.right_child=None
			else:
				self.root=None

		# CASE 2 (Node has a single child)
		if node_children==1:

			# get the single child Node
			if Node.left_child!=None:
				child=Node.left_child
			else:
				child=Node.right_child

			if node_parent!=None:
				# replace the Node to be deleted with its child
				if node_parent.left_child==Node:
					node_parent.left_child=child
				else:
					node_parent.right_child=child
			else:
				self.root=child

			# correct the parent pointer in Node
			child.parent=node_parent

		# CASE 3 (Node has two children)
		if node_children==2:

			# get the inorder successor of the deleted Node
			successor=min_index_node(Node.right_child)

			# copy the inorder successor's index to the Node formerly
			# holding the index we wished to delete
			Node.index=successor.index

			# delete the inorder successor now that it's index was
			# copied into the other Node
			self.delete_node(successor)

			# exit function so we don't call the __inspect_deletion twice
			return

		if node_parent!=None:
			# fix the height of the parent of current Node
			node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))

			# begin to traverse back up the tree checking if there are
			# any sections which now invalidate the AVL balance rules
			self.__inspect_deletion(node_parent)

	def search(self,index):
		if self.root!=None:
			return self.__search(index,self.root)
		else:
			return False

	def __search(self,index,cur_node):
		if index==cur_node.index:
			return True
		elif index<cur_node.index and cur_node.left_child!=None:
			return self.__search(index,cur_node.left_child)
		elif index>cur_node.index and cur_node.right_child!=None:
			return self.__search(index,cur_node.right_child)
		return False 

	def __inspect_insertion(self,cur_node,path=[]):
		if cur_node.parent==None: return
		path=[cur_node]+path

		left_height =self.get_height(cur_node.parent.left_child)
		right_height=self.get_height(cur_node.parent.right_child)

		if abs(left_height-right_height)>1:
			path=[cur_node.parent]+path
			self.__rebalance_node(path[0],path[1],path[2])
			return

		new_height=1+cur_node.height 
		if new_height>cur_node.parent.height:
			cur_node.parent.height=new_height

		self.__inspect_insertion(cur_node.parent,path)

	def __inspect_deletion(self,cur_node):
		if cur_node==None: return

		left_height =self.get_height(cur_node.left_child)
		right_height=self.get_height(cur_node.right_child)

		if abs(left_height-right_height)>1:
			y=self.taller_child(cur_node)
			x=self.taller_child(y)
			self.__rebalance_node(cur_node,y,x)

		self.__inspect_deletion(cur_node.parent)

	def __rebalance_node(self,z,y,x):
		if y==z.left_child and x==y.left_child:
			self.__right_rotate(z)
		elif y==z.left_child and x==y.right_child:
			self.__left_rotate(y)
			self.__right_rotate(z)
		elif y==z.right_child and x==y.right_child:
			self.__left_rotate(z)
		elif y==z.right_child and x==y.left_child:
			self.__right_rotate(y)
			self.__left_rotate(z)
		else:
			raise Exception('__rebalance_node: z,y,x Node configuration not recognized!')

	def __right_rotate(self,z):
		sub_root=z.parent 
		y=z.left_child
		t3=y.right_child
		y.right_child=z
		z.parent=y
		z.left_child=t3
		if t3!=None: t3.parent=z
		y.parent=sub_root
		if y.parent==None:
				self.root=y
		else:
			if y.parent.left_child==z:
				y.parent.left_child=y
			else:
				y.parent.right_child=y		
		z.height=1+max(self.get_height(z.left_child),
			self.get_height(z.right_child))
		y.height=1+max(self.get_height(y.left_child),
			self.get_height(y.right_child))

	def __left_rotate(self,z):
		sub_root=z.parent 
		y=z.right_child
		t2=y.left_child
		y.left_child=z
		z.parent=y
		z.right_child=t2
		if t2!=None: t2.parent=z
		y.parent=sub_root
		if y.parent==None: 
			self.root=y
		else:
			if y.parent.left_child==z:
				y.parent.left_child=y
			else:
				y.parent.right_child=y
		z.height=1+max(self.get_height(z.left_child),
			self.get_height(z.right_child))
		y.height=1+max(self.get_height(y.left_child),
			self.get_height(y.right_child))

	def get_height(self,cur_node):
		if cur_node==None: return 0
		return cur_node.height

	def taller_child(self,cur_node):
		left=self.get_height(cur_node.left_child)
		right=self.get_height(cur_node.right_child)
		return cur_node.left_child if left>=right else cur_node.right_child
