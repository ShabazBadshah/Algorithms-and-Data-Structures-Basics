class Node:
    def __init__(self, data, next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data

    def next(self):
        return self.next_node
    
    def set_next(self, next_node_to_set):
        self.next_node = next_node_to_set

    def __str__(self):
        return str(self.data) + "->" + str(self.next_node)

def reverse_linked_list(head):
    if not head:
        return None

    if not head.next():
        return head

    next_node=head.next()
    prev=None
    curr=head

    while(next_node):
        next_node=curr.next()
        curr.set_next(prev)
        prev=curr
        curr=next_node
    return prev


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.set_next(b)
b.set_next(c)
c.set_next(d)

print(a)

print(reverse_linked_list(a))
