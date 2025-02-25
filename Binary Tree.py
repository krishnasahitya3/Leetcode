class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
        
if __name__ == '__main__':
    root = Node(1)
    
    root.left = Node(2)
    root.right = Node(3)
    

    
# Python3 implementation of tree using array
# numbering starting from 0 to n-1.
tree = [None] * 10


def root(key):
	if tree[0] != None:
		print("Tree already had root")
	else:
		tree[0] = key


def set_left(key, parent):
	if tree[parent] == None:
		print("Can't set child at", (parent * 2) + 1, ", no parent found")
	else:
		tree[(parent * 2) + 1] = key


def set_right(key, parent):
	if tree[parent] == None:
		print("Can't set child at", (parent * 2) + 2, ", no parent found")
	else:
		tree[(parent * 2) + 2] = key


def print_tree():
	for i in range(10):
		if tree[i] != None:
			print(tree[i], end="")
		else:
			print("-", end="")
	print()


# Driver Code
root('A')
set_left('B', 0)
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()

   
# Python3 program to find the maximum depth of tree

# A binary tree node


class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


def maxDepth(node):
	if node is None:
		return 0

	else:

		# Compute the depth of each subtree
		lDepth = maxDepth(node.left)
		rDepth = maxDepth(node.right)

		# Use the larger one
		if (lDepth > rDepth):
			return lDepth+1
		else:
			return rDepth+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Height of tree is %d" % (maxDepth(root)))

# This code is contributed by Amit Srivastav
