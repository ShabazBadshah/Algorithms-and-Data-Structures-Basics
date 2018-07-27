'''
Given an array that has been shifted an unspecified amount
of times, find the amount of times the array has been shifted
for some given number.

If the number is not in the list, return -1, otherwise return the
shifted amount
'''

'''
Note: 
This solution is suboptimal as it runs in O(n) time, but it can
be run in O(log n) time if the findPivot function is changed from 
a linear search to a binary search (since our array is sorted)
'''

def shiftedArrSearch(shiftArr, num):
    pivot = findPivot(shiftArr)

    if(pivot == 0 or num < shiftArr[0]):
        return binarySearch(shiftArr, pivot, len(shiftArr) - 1, num)
    
    return binarySearch(shiftArr, 0, pivot - 1, num)

def findPivot(shiftArr):
  shiftAmt = 1
  for i in range(len(shiftArr) - 1):
    if shiftArr[i + 1] <= shiftArr[i]:
      break
    else:
      shiftAmt += 1
  return shiftAmt


def binarySearch(arr, begin, end, num):
    while (begin <= end):
        mid = begin + (end - begin)//2
        if (arr[mid] < num):
            begin = mid + 1
        elif (arr[mid] == num):
            return mid
        else:
            end = mid - 1

    return -1

arr = [9, 12, 17, 2, 4, 5]
print (shiftedArrSearch(arr, 2)) # 3
print (shiftedArrSearch(arr, 12)) # 1
print (shiftedArrSearch(arr, 17)) # 2
print (shiftedArrSearch(arr, 4)) # 4
print (shiftedArrSearch(arr, -1)) # -1