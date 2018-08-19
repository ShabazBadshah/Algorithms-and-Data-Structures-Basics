'''
Given an shiftArray that has been shifted an unspecified amount
of times, find the amount of times the shiftArray has been shifted
for some given number.

If the number is not in the list, return -1, otherwise return the
shifted amount

Runs in O(log n)
'''


def shiftedArrSearch(shiftArr, num):
  pivot = findPivot(shiftArr)

  if(pivot == 0 or num < shiftArr[0]):
    return binarySearch(shiftArr, pivot, len(shiftArr) - 1, num)

  return binarySearch(shiftArr, 0, pivot - 1, num)


def findPivot(shiftArr):
  begin = 0
  end = len(shiftArr) - 1

  while begin <= end:
    mid = begin + (end - begin) // 2
    if mid == 0 or shiftArr[mid] < shiftArr[mid - 1]:
      return mid
    if shiftArr[mid] > shiftArr[0]:
      begin = mid + 1
    else:
      end = mid - 1

  return 0


def binarySearch(shiftArr, begin, end, num):
  while (begin <= end):
    mid = begin + (end - begin)//2
    if (shiftArr[mid] < num):
      begin = mid + 1
    elif (shiftArr[mid] == num):
      return mid
    else:
      end = mid - 1

  return -1


shiftArr = [9, 12, 17, 2, 4, 5]
print (shiftedArrSearch(shiftArr, 2))  # 3
print (shiftedArrSearch(shiftArr, 12))  # 1
print (shiftedArrSearch(shiftArr, 17))  # 2
print (shiftedArrSearch(shiftArr, 4))  # 4
print (shiftedArrSearch(shiftArr, -1))  # -1
