class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    
    def __init__(self):
        self.__head = None
        self.__length = 0
        

    def insert(self, data):
        node = Node(data)
        
        if self.__head == None: # add new node as head
            self.__head = node
        else: 
            node.next = self.__head
            node.next.prev = node
            self.__head = node
            
        self.__length += 1

    def update(self, x, data):
        change_node = self.search(x)

        if (change_node == None):
            return False
        change_node.data = data
        return True
        

    def remove(self, x):
        rm_node = self.search(x)
        
        if (rm_node == None):
            return None

        if rm_node == self.__head: # Removing head
            self.__head = rm_node.next
        elif rm_node.next == None: # Removing tail
            rm_node.prev.next = None
        else: # Removing anything else that is not the head or tail
            rm_node.prev.next = rm_node.next
            rm_node.next.prev = rm_node.prev
    
        self.__length -=1
        return rm_node
    

    def search(self, x):
        curr_node = self.__head
        
        while (curr_node != None):
            if curr_node.data == x:
                return curr_node
            curr_node = curr_node.next
            
        return None


    def size(self):
        return self.__length


    def __str__(self):

        if self.size() == 0:
            return "List is empty"
        
        ret_str = ""
        seperator = "<->"
        
        curr_node = self.__head
        
        while (curr_node != None):
            ret_str += "{0}{1}".format(str(curr_node), seperator)
            curr_node = curr_node.next

        # Removes the last item's seperator and returns the rest of the string
        return ret_str[:len(ret_str) - len(seperator)]


ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(-23)
ll.insert(42)
ll.insert(32)

print (ll)

print(ll.search(1))
print(ll.search(2))
print(ll.search(3))

ll.remove(-1)
print(ll)

print(ll.remove(3))
print(ll.remove(-23))
print(ll.remove(42))
print(ll.update(1, 2))
print(ll.remove(1))
print(ll)

print(ll.size())
print(ll.remove(2))
print(ll)
print(ll.remove(32))
print(ll)
print(ll.size())
print(ll.remove(2))
print(ll)
