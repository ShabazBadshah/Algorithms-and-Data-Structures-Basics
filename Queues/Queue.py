class Queue():

    def __init__(self):
        self.__array = []
        self.__size = 0

    def enqueue(self, x):
        self.__size += 1
        self.__array.append(x)

    def front(self):
        if (self.__size > 0):
            return self.__array[0]
        return None
        
    def dequeue(self):
        if (self.__size > 0):
            self.__size -= 1
            return self.__array.pop(0)
        return None

    def search(self, x):
        for i in range(len(self.__array)):
            if (self.__array[i] == x):
                return self.__array[i]
        return None

    def size(self):
        return len(self.__array)

    def __len__(self):
        return self.__size
    
    def __str__(self):
        return str(self.__array)


q = Queue()

print(q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.front())
print(q.dequeue())
print(q)
print(q.front())
printS
print(q.search(3))
print(q)
print(q.search(2))
print(q.dequeue())
print(q.dequeue())
print(q)
