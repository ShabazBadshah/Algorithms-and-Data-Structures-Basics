class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

'''
Binary Search Tree Property:

For any given node, all nodes in the left subtree will have values that are
strictly less than the root. All nodes in the right subtree will have values
that are greater than or equal to the root's value

Space Complexity: O(n)
'''
class BST:
    def __init__(self):
        self.__root = None

    '''
    Finds the smallest element in the BST
    Runtime: O(n) worst case, O(log n) average case
    '''
    def minimum(self):
        return self.__minimum(self.__root)
    def __minimum(self, root):
        if root is None or root.left is None:
            return root.data
        return self.__minimum(root.left)

    '''
    Finds the maximum element in the BST
    Runtime: O(n) worst case, O(log n) average case
    '''
    def maximum(self):
        return self.__maximum(self.__root)
    def __maximum(self, root):
        if root is None or root.right is None:
            return root.data
        return self.__maximum(root.right)


    '''
    Inserts the given Node into the BST
    Runtime: O(n) worst case, O(log n) average case
    '''
    def insert(self, value):
        return self.__insert(self.__root, value)
    def __insert(self, root, value):
        if root is None:
            self.__root = Node(value)
            # return True
        else:
            if value >= root.data:
                if root.right is not None:
                    self.__insert(root.right, value)
                else:
                    root.right = Node(value)
                    # return True
            elif value < root.data:
                if root.left is not None:
                    self.__insert(root.left, value)
                else:
                    root.left = Node(value)
                    # return True
         
        # return False


    def delete(self, root, data):
        pass


    '''
    Finds and returns the given Node in the BST
    Runtime: O(n) worst case, O(log n) average
    '''
    def search(self, element_to_find):
        return self.__search(self.__root, element_to_find)

    def __search(self, root, element_to_find):
        if root == None:
            return None

        if root.data == element_to_find:
            return root.data

        if element_to_find >= root.data:
            return self.__search(root.right, element_to_find)
        else:
            return self.__search(root.left, element_to_find)


    '''
    Returns the root of the BST
    Runtime: O(1)
    '''
    def get_root(self):
        return self.__root


    '''
    Runs a preorder traversal on the BST
    Runtime: O(n)
    '''
    def preorder(self):
        return self.__preorder(self.__root)
    def __preorder(self, root):
        if root:
            print (root.data)
            self.__preorder(root.left)
            self.__preorder(root.right)


    '''
    Runs a inorder traversal on the BST
    Runtime: O(n)
    '''
    def inorder(self):
        return self.__inorder(self.__root)    
    def __inorder(self, root):
        if root:
            self.__inorder(root.left)
            print (root.data)
            self.__inorder(root.right)


    '''
    Runs a postorder traversal on the BST
    Runtime: O(n)
    '''
    def postorder(self):
        return self.__postorder(self.__root)
    def __postorder(self, root):
        if root:
            self.__postorder(root.left)
            self.__postorder(root.right)
            print (root.data)


bst = BST()
bst.insert(2)
bst.insert(5)
bst.insert(3)
bst.insert(1)
bst.insert(4)

print ("Minimum: " + str(bst.minimum()))
print ("Maximum: " + str(bst.maximum()) + "\n")
print("Searching for element 1:     " + str(bst.search(1)))
print("Searching for element 2:     " + str(bst.search(2)))
print("Searching for element -2:    " + str(bst.search(-2)))

print ("\nPreorder Traversal:")
bst.preorder()

print ("Postorder Traversal:")
bst.postorder()

print ("Inorder Traversal:")
bst.inorder()