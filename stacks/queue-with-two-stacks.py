'''
Implement a Queue using two Stacks
'''

class Queue(object):
  def __init__(self):
    self.tempStack=[]
    self.stack=[]

  def enqueue(self,element):
    self.tempStack.append(element)

  def dequeue(self):
    if not self.stack:
      while self.tempStack:
        self.stack.append(self.tempStack.pop())
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