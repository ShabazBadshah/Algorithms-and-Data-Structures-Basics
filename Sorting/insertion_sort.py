
'''
Runtime: O(n^2)
Runtime Avg Case: O(n^2)
Best Case: O(n)
Space: O(1)
'''
def insertion_sort(arr):

    for i in range(0, len(arr)):

        curr_el = arr[i]
        pos = i

        while (pos > 0 and arr[pos - 1] > curr_el):
            arr[pos]=arr[pos - 1]
            pos -= 1
        arr[pos] = curr_el

    return arr


array = [9, 3, 4, 1, 7, 2, 10, 6, 8, 5]
print(insertion_sort(array))
