'''
Implement a Queue using two Stacks
'''

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

class Queue():
  def __init__(self):
    self.tempStack = Stack()
    self.stack = Stack()

  def enqueue(self,element):
    self.tempStack.push(element)

  def dequeue(self):
    if not self.stack:
      while self.tempStack:
        self.stack.push(self.tempStack.pop())
    return self.stack.pop()

  def __str__(self):
    return str(self.stack)


queue = Queue()
queue.enqueue(3)
queue.enqueue(1)
queue.enqueue(14)
queue.enqueue(-3)
print (queue)
print ("Dequeued: " + str(queue.dequeue()))
print (queue)
queue.enqueue(-1337)
print ("Dequeued: " + str(queue.dequeue()))
print ("Dequeued: " + str(queue.dequeue()))
print (queue)
