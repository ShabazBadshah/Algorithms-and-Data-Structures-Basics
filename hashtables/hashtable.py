import math

class Hashtable:

  def __init__(self, size = 32):
    # Gets the next highest number that is a power of 2
    self.__size = 2 ** (int(math.ceil(math.log(size)/math.log(2))))
    self.__table = self.__size * [None]

  def __get_index(self, element):
    return hash(element) % self.__size

  def get(self, element):
    idx = self.__get_index(element)

    if type(self.__table[idx]) == list:
      return element in self.__table[idx]
    else:
      return self.__table[idx] == element

    return None

  def put(self, element):
    idx = self.__get_index(element)

    if not self.__table[idx]:
      self.__table[idx] = element
    else:
      if type(self.__table[idx]) == list:
        self.__table[idx] = [self.__table[idx], element]
      else:
        self.__table.append(element)

  def delete(self, element):
    idx = self.__get_index(element)

    if self.__table[idx] != None:
      if type(self.__table[idx]) == list:
        element_idx = self.__table[idx].index(element)
        self.__table[idx][element_idx] = None
      else:
        self.__table[idx] = None
    else:
      raise KeyError("element" + str(element) + "can't be found")

  def __str__(self):
    return str(self.__table)

h = Hashtable(20)
h.put('abc')
print(h.get('abc'))
h.delete('abc')
print(h.get('abc'))
