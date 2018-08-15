def look_and_say(n):
  '''
  Return the nth term in the 'look and say sequence'
  
  :type n: Integer
  :rtype: String

  Look and Say Sequence (https://www.wikiwand.com/en/Look-and-say_sequence)

  Sequence: 1, 11, 21, 1211, 111221, 312211, 13112221

  1 is read off as "one 1" or 11.
  11 is read off as "two 1s" or 21.
  21 is read off as "one 2, then one 1" or 1211.
  1211 is read off as "one 1, one 2, then two 1s" or 111221.
  111221 is read off as "three 1s, two 2s, then one 1" or 312211.
  '''

  result = "1"
  for i in range(n):
    result = generate_next_num(result)
  return result

def generate_next_num(s):

  i = 0
  result = ""

  while i < len(s):
    count = 1
    while i < len(s) - 1 and s[i] == s[i + 1]:
      i += 1
      count += 1
    result += str(count) + s[i]
    i += 1
  return result


print (look_and_say(1))
print (look_and_say(2))
print (look_and_say(3))
print (look_and_say(4))
print (look_and_say(5))
print (look_and_say(6))
print (look_and_say(7))
print (look_and_say(8))
print (look_and_say(9))
print (look_and_say(10))