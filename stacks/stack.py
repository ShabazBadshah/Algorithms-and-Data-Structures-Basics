class Stack():

    def __init__(self):
        self.__array = []
        self.__size = 0

    def push(self, x):
        self.__size += 1
        self.__array.append(x)
        
    def pop(self):
        if (self.__size > 0):
            self.__size -= 1
            return self.__array.pop()
        return None

    def update(self, x, data):
        for i in range(len(self.__array)):
            if (x == self.__array[i]):
                self.__array[i] = data
                return True
        return False 

    def search(self, x):
        for i in range(len(self.__array)):
            if (x == self.__array[i]):
                return self.__array[i]
        return None

    def peek(self):
        if (self.__size > 0):
            return self.__array[self.__size - 1]
        return None

    def size(self):
        return len(self.__array)

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.__array)


s = Stack()
s.push(1)
s.push(2)
s.push(-3)
s.push(42)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s.peek())
print(s)
print(s.size())
print
print(s.search(-99))
print(s.search(-3))
print (s.update(2, -3))
print(s.search(-3))
print(s.search(2))
print(s)
