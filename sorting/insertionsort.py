'''
Runtime Worst Case: O(n^2)
Runtime Avg Case: O(n^2)
Runtime Best Case: O(n)
Space: O(1)
'''

'''
The crux of insertion sort is comparable to sorting a deck of cards. The algorithm keeps a 
sorted and unsorted list. Similarly to how you may sort a deck of cards, the algorithm will 
pick the next element from the unsorted part of the list and 'insert' it into the correct spot
in the sorted part of the list. This repeats until the list is sorted 
'''

def insertion_sort(arr):

    for i in range(0, len(arr)):

        curr_el = arr[i]
        pos = i

        while (pos > 0 and arr[pos - 1] > curr_el):
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1
        arr[pos] = curr_el

    return arr


array = [9, 3, 4, 1, 7, 2, 10, 6, 8, 5]
print(insertion_sort(array))
