class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.__data = data
        self.__left_child = left_child
        self.__right_child = right_child

    def left_child(self):
        return self.__left_child

    def right_child(self):
        return self.__right_child

    def set_left_node(self, new_left_child):
        self.__left_child = new_left_child

    def set_right_node(self, new_right_child):
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


n0 = Node(3)
print n0
n1 = Node(2)
n2 = Node(4, n0, n1)
print n1
print n2
n0.set_left_node(n1)
print n2
