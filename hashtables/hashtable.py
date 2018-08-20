import math

class Hashtable:
  def __init__(self, size = 32):
    # Gets the next highest number that is a power of 2
    self.__size = 2 ** (int(math.ceil(math.log(size)/math.log(2))))
    self.__table = [[] for _ in range(self.__size)]

  def __get_index(self, element):
    return hash(element) % self.__size

  def get(self, element):
    idx = self.__get_index(element)
    return element in self.__table[idx]

  def put(self, element):
    idx = self.__get_index(element)
    self.__table[idx].append(element)

  def delete(self, element):
    idx = self.__get_index(element)
    try:
      element_idx = self.__table[idx].index(element)
      self.__table[idx][element_idx] = None
    except ValueError:
      raise KeyError("KeyError: " + str(element) + " was not found")

  def __str__(self):
    return str(self.__table)

h = Hashtable(30)
h.put('abc')
print(h.get('abc')) # True
h.delete('abc') 
print(h.get('abc')) # False
print(h.delete('abc')) # Raises KeyError, program terminates