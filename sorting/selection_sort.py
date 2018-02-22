'''
Runtime Worst Case: O(n^2)
Runtime Avg Case: O(n^2)
Runtime Best Case: O(n^2)
Space: O(1)
'''

'''
Selection sort is very similar to insertion sort in terms of keeping track of a sorted and
unsorted array, however selection sort differs in the way it adds elements to the sorted portion
of the array. More specifically, selection sort will 'select' the minimum element from the 
unsorted array and appends it to the sorted portion of the array. 

Ex.

sorted              sorted                  sorted
 v                    v                       v
[3, | 9, 7, 5] -> [3, 5, | 9, 7] -> [3, 5, 7, | 9] -> [3, 5, 9, 7]

'''

def selection_sort(arr):

    for i in range(len(arr)):
        
        max_ind = i
        j = i

        while (j < len(arr)): 
            if (arr[j] > arr[max_ind]): 
                max_ind = j
            j += 1

        arr[i], arr[max_ind] = arr[max_ind], arr[i]     

    return arr


array = [9, 3, 4, 1, 7, 2, 10, 6, 8, 5]
print(selection_sort(array))