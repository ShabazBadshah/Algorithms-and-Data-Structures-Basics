def longestSubstringLength(s):
  '''
  Given a string s, return the longest substring in s that does
  not have repeating characters

  e.g.
  abcabccbb -> 3, abc is the longest substring
  bbbbbbbbb -> 1, b is the longest substring
  qwerty ->  5, qwerty is the longest substring

  Runs in O(n) time
  '''

  if not s or s == "":
    return 0

  if len(s) == 1:
    return 1

  maxSubstringLen = 0
  tempStr = ""

  for letter in s:
    if letter not in tempStr:
      tempStr += letter
      if len(tempStr) > maxSubstringLen:
        maxSubstringLen = len(tempStr)
      else:
        tempStr = tempStr[tempStr.index(letter) + 1:] + letter
  return maxSubstringLen

print (longestSubstringLength("abcabcbb")) #3
print (longestSubstringLength("bbbbbbbb")) #1
print (longestSubstringLength("qwerty")) #6
