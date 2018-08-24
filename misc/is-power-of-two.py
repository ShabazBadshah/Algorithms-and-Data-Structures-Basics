import math

'''
Given an integer, write a function to determine if it is a power of two.
Runtime:
  Time: O(1)
  Space: O(1)
'''
def isPowerOfTwo(n):
  return n > 0 and 2 ** round(math.log(n, 2)) == n

print (isPowerOfTwo(16)) # True
print (isPowerOfTwo(8)) # True
print (isPowerOfTwo(4)) # True
print (isPowerOfTwo(2)) # True
print (isPowerOfTwo(1)) # True
print (isPowerOfTwo(0)) # False
print (isPowerOfTwo(33)) # False
print (isPowerOfTwo(18)) # False
print (isPowerOfTwo(3)) # False
print (isPowerOfTwo(-1)) # False