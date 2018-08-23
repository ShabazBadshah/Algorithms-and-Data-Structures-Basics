def plusOne(digits):
  '''
  Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
  The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
  You may assume the integer does not contain any leading zero, except the number 0 itself.

  E.g.
  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
  [1, 2, 3] -> [1, 2, 4]
  [0] -> [1]
  [9] -> [1, 0]

  Runtime:
    Time: O(n)
    Space: O(1)
  '''

  carryOne = 1

  for i in range(len(digits) - 1, -1, -1):
    if digits[i] == 9 and carryOne == 1:
      digits[i] = 0
      carryOne = 1
    else:
      digits[i] += carryOne
      carryOne = 0


  if carryOne == 1:
    digits = [1] + digits
  return digits

digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print (plusOne(digits))