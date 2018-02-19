'''
Runtime Worst Case: O(n^2)
Runtime Avg Case: O(n^2)
Runtime Best Case: O(n^2)
Space: O(1)
'''

def selection_sort(arr):

    for i in range(len(arr)):
        
        max_ind = i
        j = i

        while (j < len(arr)):
            if (arr[j] > arr[max_ind]): max_ind = j
            j += 1

        arr[i], arr[max_ind] = arr[max_ind], arr[i]     

    return arr


array = [9, 3, 4, 1, 7, 2, 10, 6, 8, 5]
print(selection_sort(array))