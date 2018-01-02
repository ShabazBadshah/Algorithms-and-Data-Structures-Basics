'''
Sorts the list from least to greatest

Runtime: O(n^2)
Space: O(1)
'''
def bubble_sort(arr_to_sort):

    for i in range(len(arr_to_sort)):
        for j in range(len(arr_to_sort) - 1):
            if arr_to_sort[i] < arr_to_sort[j]:
                arr_to_sort[i], arr_to_sort[j] = arr_to_sort[j], arr_to_sort[i]
    
    return arr_to_sort

l = [12, 11, 13, 5, 6, 7, -1, -5356]
print bubble_sort(l)
