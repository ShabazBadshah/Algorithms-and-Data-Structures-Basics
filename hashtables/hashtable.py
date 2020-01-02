class Hashtable: 
  def __init__(self, size=1):
    self.size = size
    self.number_of_keys = 0
    self.table = [(None, None)] * self.size

  def put(self, key, value):
    
    if self.size  == self.number_of_keys:
      self.expand_table()

    index = self.generate_index(key)

    if self.table[index][0] == None:
      self.table[index] = (key, value)
      self.number_of_keys += 1
    else:
      current_key = self.table[index][0]
      # updating existing value
      if current_key == key:
        self.table[index] = (key, value)
      else:
        while self.table[index % self.size][0] != None:
          index += 1
        self.table[index] = (key, value)
        self.number_of_keys += 1
      
  def get(self, key):
    index = self.generate_index(key)
    if self.table[index][0] == key:
      return self.table[index][1]
    else:
      key_index = self.find_in_table(key)
      if key_index == -1:
        raise KeyError(str(key) + " not found")
      else:
        print key_index
        return self.table[key_index][1]

  def find_in_table(self, key):
    index = self.generate_index(key)
    counter = 0
    while self.table[index % self.size][0] != key:
      index += 1
      counter += 1
      if counter == self.size:
        return -1
    return index

  def delete(self, key):	
    key_index = self.find_in_table(key)
    if key_index == -1:
      raise KeyError(str(key) + " not found")
    else:	
      self.table[key_index] = (None,None) 
      self.number_of_keys -= 1

  def expand_table(self):
    self.table += [(None,None)] * self.size
    self.size = len(self.table)

  def generate_index(self, key):
    return hash(key) % self.size

  def __str__(self):
    return str(self.table)

h = Hashtable()
h.put('abc', 'def')
# print (h)
# print(h.get('abc')) # True
h.put('abc', 6)
h.put('abc', 4)
h.put('eoefoef', 5)
h.put('abc', 343)
# h.delete('abc')
# h.get('abc')
print (h)
