'''
Runtime Worst Case: O(n^2)
Runtime Avg Case: O(n^2)
Runtime Best Case: O(n)
Space: O(1)
'''

'''
Bubble sort works by swapping an element with the one adjacent to it until it is in its correct
position (in their correct sorted position in the array). It keeps doing this with every 
element until the entire array is sorted.
'''

def bubble_sort(arr_to_sort):

    for i in range(len(arr_to_sort)):
        for j in range(len(arr_to_sort) - 1):
            if arr_to_sort[i] < arr_to_sort[j]:
                arr_to_sort[i], arr_to_sort[j] = arr_to_sort[j], arr_to_sort[i]
    
    return arr_to_sort

l = [12, 11, 13, 5, 6, 7, -1, -5356]
print bubble_sort(l)
l = ['F', 'C', 'A', 'Z', 'W']
print bubble_sort(l)

