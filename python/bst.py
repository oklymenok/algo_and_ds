
class Node():

	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class BST():

	def __init__(self,root):
		self.root = root

	def search(self,val):
		root = self.root
		return self._search(root,val)

	def _search(self,root,val):
		if root == None or root.val == val:
	 		return root
		elif root.val > val:
			return self._search(root.left,val)
		else:
			return self._search(root.right,val)

	def insert(self,node):
		root = self.root
		self._insert(root,node)
	
	def _insert(self,root,node):
		if root == None:
			root = node
		elif root.val == node.val:
			print "Node already exists"
		elif root.val > node.val and root.left != None:
			self._insert(root.left,node)
		elif root.val > node.val and root.left == None:
			root.left = node
		elif root.val < node.val and root.right != None:
			self._insert(root.right,node)
		elif root.val < node.val and root.right == None:
			root.right = node

	def printInOrder(self):
		node = self.root
		self._printInOrder(node)

	def _printInOrder(self,root):
		if root.left != None:
			self._printInOrder(root.left)
		print root.val
		if root.right != None:
			self._printInOrder(root.right)


#		    10
#           5               20
#       3       9       15       25

n1 = Node(10)
n2 = Node(5)
n3 = Node(20)
n4 = Node(3)
n5 = Node(9)
n6 = Node(15)
n7 = Node(25)
n8 = Node(30)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

print "*** Create a new Binary Search Tree"
the_tree = BST(n1)
print "*** Searching for node with value 20"
node = the_tree.search(20)
if node != None:
	print node
print "*** InOrder BST traversal"
the_tree.insert(n8)
the_tree.printInOrder()
