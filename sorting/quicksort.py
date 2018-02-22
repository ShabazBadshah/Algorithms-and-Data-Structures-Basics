'''
Runtime Worst Case: O(n^2)
Runtime Avg Case: O(n log n)
Runtime Best Case: O(n log n)
Space: O(1)
'''

'''
Quicksort works by splitting up the array via a pivot. All elements less than the pivot are 
moved to the left of a pivot, and all the elements larger are moved to the right. The algorithm
is recursively called on the sub-arrays of the pivot until the entire array is sorted.
Mergesort is similar to Quicksort, except it does not use constant space, Quicksort is an
in-place sorting algorithm.
'''

def quicksort(arr):
	return quicksort_helper(arr,0,len(arr)-1)

def quicksort_helper(arr,left_ind,right_ind):

	if left_ind<right_ind:
		pivot = partition(arr,left_ind, right_ind)
		quicksort_helper(arr, left_ind, pivot - 1)
		quicksort_helper(arr, pivot + 1,right_ind)
	return arr

def partition(arr, left_ind, right_ind):

	pivotvalue = arr[left_ind]
	leftmark = left_ind + 1
	rightmark = right_ind
	done = False

	while not done:
		while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark - 1

		if rightmark < leftmark: done = True
		else: arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

	arr[left_ind], arr[rightmark] = arr[rightmark], arr[left_ind]

	return rightmark

array = [9, 3, 4, 1, 7, 2, 10, 6, 8, 5]
print(quicksort(array))
