from itertools import permutations

'''(
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''

def isPalindrome(string):
  for i in range(len(string)):
    if string[i] != string[len(string) - i - 1]:
      return False
  return True

# Brute Force O(n!) runtime
def palindromePermutationBad(string):
  allPerms = set([''.join(p) for p in permutations(string)])

  for permutation in allPerms:
    if isPalindrome(permutation):
      return True

  return False
  
print (palindromePermutationBad("code")) # False
print (palindromePermutationBad("aab")) # True
print (palindromePermutationBad("carerac")) # True

