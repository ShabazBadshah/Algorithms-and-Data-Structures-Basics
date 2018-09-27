def numUniqueBinaryTrees(n):

  if n < 0:
    return 0

  if n == 1:
    return 1

  previousSolutions = [0] * (n + 1)
  previousSolutions[0] = 1
  for i in range(1, n + 1):
    for j in range(i):
      previousSolutions[i] += previousSolutions[j] * previousSolutions[i - j - 1]
  return previousSolutions[n]

print (numUniqueBinaryTrees(1))
print (numUniqueBinaryTrees(2))
print (numUniqueBinaryTrees(3))
print (numUniqueBinaryTrees(4))
print (numUniqueBinaryTrees(5))