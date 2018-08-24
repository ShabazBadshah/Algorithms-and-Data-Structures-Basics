'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:
  def __init__(self):
    self.data = []
    self.minElement = None

  def push(self, x):
    """
    :type element: int
    :rtype: void

    Time: O(1)
    """

    if self.minElement == None:
      self.minElement = x

    self.minElement = min(self.minElement, x)
    self.data.append((x, self.minElement))

  def pop(self):
    """
    :rtype: void

    Time: O(1)
    """ 
    if self.data:
      self.data.pop()

  def top(self):
    """
    :rtype: void

    Time: O(1)
    """ 
    if self.data:
      return self.data[len(self.data) - 1]
    return None

  def getMin(self):
    """
    :rtype: void

    Time: O(1)
    """ 
    return self.top()[1]


minStack = MinStack()
minStack.push(3)
minStack.push(1)
minStack.push(14)
minStack.push(-3)
print (minStack.getMin()) # -3
minStack.pop()
print (minStack.getMin()) # 1
minStack.push(-1337)
print (minStack.getMin()) # -1337