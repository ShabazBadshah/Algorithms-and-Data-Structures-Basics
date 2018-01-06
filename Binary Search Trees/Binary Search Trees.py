class node:
    def __init__(self, data, left_child=None, right_child=None):
        self.__data = data
        self.__left_child = left_child
        self.__right_child = right_child

    def left_child(self):
        return self.__left_child

    def right_child(self):
        return self.__right_child

    def set_left_child(self, new_left_child):
        self.__left_child = new_left_child

    def set_right_child(self, new_right_child):
        self.__right_child = new_right_child

    def get_data(self):
        return self.__data

    def __str__(self):

        left_str = str(self.__left_child)
        right_str = str(self.__right_child)

        if left_str == "None":
            left_str = ""
        if right_str == "None":
            right_str = ""

        return "[{0}:{1}:{2}]".format(self.__data, left_str, right_str)


'''
Binary Search Tree Property:

For any given node, all nodes in the left subtree will have values that are
strictly less than the root. All nodes in the right subtree will have values
that are greater than or equal to the root's value

Space Complexity: O(n)
'''
class binary_search_tree:
    def __init__(self, root):
        self.__root = root

    '''
    Runtime: O(n) worst case, O(log n) average
    '''
    def insert(self, root, node):

        if root == None:
            root = node
            return True
        else:
            if node.get_data() >= root.get_data():
                if root.left_child() == None:
                    root.set_left_child(node)
                    return True
                else:
                    return self.insert(root.left_child(), node)
            else:
                if root.right_child() == None:
                    root.set_right_child(node)
                    return True
                else:
                    return self.insert(root.right_child(), node)
        return False


    def delete(self, root, node):
        pass

    '''
    Runtime: O(n) worst case, O(log n) average
    '''
    def search(self, node, element_to_find):

        if node.get_data() == element_to_find:
            return node

        if element_to_find >= node.get_data():
            return search(node.right_child(), element_to_find)
        else:
            return search(node.left_child(), element_to_find)

        return None


    '''
    Runtime: O(1)
    '''
    def get_root(self):
        return self.__root

    def __str__(self):
        return str(self.__root)

root = node(0)
n1 = node(2)
n2 = node(1)
n3 = node(-1)
n4 = node(-2)

bst = binary_search_tree(root)
print bst
print bst.insert(root, n1)
print bst.insert(root, n2)
print bst.insert(root, n3)
print bst.insert(root, n4)
print bst
