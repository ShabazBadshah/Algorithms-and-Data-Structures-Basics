
'''
Given an array, the function will return a list of all pair of 
numbers that add to 100
'''
def add_to_one_hundred(arr):
  
  foundSet = {}
  results = []
  for i in range(len(arr)):
    foundSet[arr[i]] = arr[i]

  for j in range(len(arr)):
    if ((100 - arr[j]) in foundSet and ([100 - arr[j], arr[j]]) not in results):
      results.append([100 - arr[j], arr[j]])
  
  return results

arr = [0, 1, 100, 99, 0, 10, 90, 30, 55, 33, 55, 75, 50, 51, 49, 50, 51, 49, 51]
print ("----- Add to One Hundred -----")
print (add_to_one_hundred(arr))