def heapify(arr_to_sort, ind, heap_size):
    largest = ind
    left_child_ind = (2 * ind) + 1
    right_child_ind = (2 * ind) + 2
    
    if left_child_ind < heap_size and arr_to_sort[left_child_ind] > arr_to_sort[largest]:
        largest = left_child_ind

    if right_child_ind < heap_size and arr_to_sort[right_child_ind] > arr_to_sort[largest]:
        largest = right_child_ind

    if largest != ind:
        arr_to_sort[largest], arr_to_sort[ind] = arr_to_sort[ind], arr_to_sort[largest]
        heapify(arr_to_sort, largest, heap_size)

'''
Runtime: O(n log n)
Space: O(1)
'''
def heapsort(arr_to_sort):

    # Bulds max heap
    for i in range(len(arr_to_sort) // 2 - 1, -1, -1):
        heapify(arr_to_sort, i, len(arr_to_sort))

    # Sorts the heap 
    for i in range(len(arr_to_sort) - 1, 0, -1):
        arr_to_sort[0], arr_to_sort[i] = arr_to_sort[i], arr_to_sort[0]
        heapify(arr_to_sort, 0, i)
        
    return arr_to_sort

l = [12, 11, 13, 5, 6, 7, -1]
print heapsort(l)
