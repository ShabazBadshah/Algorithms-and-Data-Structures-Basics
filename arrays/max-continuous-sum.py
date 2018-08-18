
def maxContinuousSum(arr):
  '''
  Given an array, return the maximum continuous sum
  Runs in O

  E.g. Given [-1,4,-3,5,7], returns 12 (5 + 7 is the maximum sum)
  '''

  maxSum = 0
  currSum = 0

  for num in arr:
    currSum += num
    maxSum = max(maxSum, currSum)
      
  return maxSum

arr = [-1,4,-3,5,7]
print (maxContinuousSum(arr)) # 12