"""
Finds the first unique character in the string. Does not account for the 
different character cases (i.e. 'A' and 'a' are both the same letter)

param: word, the string which is going to be checked
return: 
  - None, if there is no unqiue character
  - String, the first unique letter in the word
"""
def first_non_repeating_char(word):

  if len(word) <= 1:
    return word

  word = word.lower().strip()

  word_order = []
  letter_counts = {}

  for letter in word:
    if letter in letter_counts:
      letter_counts[letter] += 1
    else:
      letter_counts[letter] = 1 
      word_order.append(letter)

  for letter in word_order:
    if letter_counts[letter] == 1:
      return letter

  return None

print("\nFirst Non-Repeating Character\n--------------------")
print("foof:    " + str(first_non_repeating_char("foof")))
print("'':      " + str(first_non_repeating_char("")))
print("a:       " + str(first_non_repeating_char("a")))
print("racecar: " + str(first_non_repeating_char("racecar")))
print("potato:  " + str(first_non_repeating_char("potato")))
print("ABCa:    " + str(first_non_repeating_char("ABC")))
print("abcdeffffffffffa:     " + str(first_non_repeating_char("abcdeffffffffffa")))