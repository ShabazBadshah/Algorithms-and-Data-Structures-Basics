class Binary_Min_Heap:
    def __init__(self):
        self.__heap = []
        self.__heap_size = 0

    def __swap_elements_at_ind(self, a, b):
        self.__heap[a], self.__heap[b] = self.__heap[b], self.__heap[a]

    def __parent(self, i):
        return (i - 1) // 2

    def __left(self, i):
        return (2 * i) + 1

    def __right(self, i):
        return (2 * i) + 2

    def __has_left_child(self, i):
        return self.__left(i) < self.__heap_size

    def __has_right_child(self, i):
        return self.__right(i) < self.__heap_size
    
    def get_min(self):
        if (self.__heap_size != 0):
            return self.__heap[0]
        return None
		
	def build_heap(self, array):
		for i in range(
		
    def insert(self, element):
        self.__heap.append(element)
        self.__heap_size += 1
        self.__heapify_up(self.__heap_size - 1)        

    def delete(self, element):
        self.swap_heap_elements(0, self.__heap_size - 1)
        ret = self.__heap.pop()
        self.__heap_size -= 1
        self.__heapify_down(0)
        return ret

    def __heapify_up(self, current):
        while current > 0 and self.__heap[current] < self.__heap[self.__parent(current)]:
            self.__swap_elements_at_ind(current, self.__parent(current))
            current = self.__parent(current)

    def __heapify_down(self, current):
        while current < self.__heap_size:
            if self.__has_left_child(current):
                small = self.__left(current)
                if self.__has_right_child(current) and self.__heap[small] > self.__heap[self.__right(current)]:
                    small = self.__right(current)
                if self.__heap[current] > self.__heap[small]:
                    self.__swap_elements_at_ind(current, small)
                    current = small
                else:
                    return
            else:
                return 

    def __str__(self):
        return str(self.__heap)

h = Binary_Min_Heap()
h.insert(9)
h.insert(5)
h.insert(6)
h.insert(2)
h.insert(3)
h.insert(-1)

#print("---")
#h.__heapify_up()

print(h)
print(h.get_min())
