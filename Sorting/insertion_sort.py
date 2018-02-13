
'''
Runtime: O(n^2)
Runtime Avg Case: O(n^2)
Best Case: O(n)
Space: O(1)
'''
def insertion_sort(arr):

    for i in range(0, len(arr)):

        key = arr[i]
        j = i - 1

        while (j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


array = [9, 3, 4, 1, 7, 2, 10, 6, 8, 5]
print(insertion_sort(array))
