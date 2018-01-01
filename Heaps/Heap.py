class Binary_Min_Heap:
    def __init__(self, array):
        self.__heap = []
        self.__heap_size = 0
        self.__build_min_heap(array)

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

    def get_heap(self):
        return self.__heap
		
    def __build_min_heap(self, array): 
        self.__heap = array[:]
        self.__heap_size = len(array)
        
        for i in range(len(array) - 1, len(array) // 2 - 1, -1):
            self.__heapify_up(i)
		
    def insert(self, element):
        self.__heap.append(element)
        self.__heap_size += 1
        self.__heapify_up(self.__heap_size - 1)        

    def extract_min(self):
        self.__swap_elements_at_ind(0, self.__heap_size - 1)
        self.__heap_size -= 1
        self.__heapify_down(0)
        return self.__heap.pop()

    def __heapify_up(self, current):
        while current > 0 and self.__heap[current] < self.__heap[self.__parent(current)]:
            self.__swap_elements_at_ind(current, self.__parent(current))
            current = self.__parent(current)

    def __heapify_down(self, current):
        while current < self.__heap_size and self.__has_left_child(current):
            smaller_element = self.__left(current)
            if self.__has_right_child(current) and self.__heap[smaller_element] > self.__heap[self.__right(current)]:
                smaller_element = self.__right(current)
            if self.__heap[current] > self.__heap[smaller_element]:
                self.__swap_elements_at_ind(current, smaller_element)
                current = smaller_element

    def __str__(self):
        return str(self.__heap)

l = [9, 5, 6, 2, 3, -1]
h = Binary_Min_Heap(l)

print h.extract_min()
print h
h.insert(-3)
print "min: {0}".format(h.get_min())
print h
