'''
Returns the element if found
otherwise returns None

Only works on sorted lists

Runtime: O(log n)
Space: O(1)
'''
def binary_search(arr_to_search, element_to_find):

    median = len(arr_to_search) // 2

    # If we found our element
    if arr_to_search[median] == element_to_find:
        return arr_to_search[median]
    # If there is only one element left in the list and its not the one we are looking for
    elif len(arr_to_search) == 1 and arr_to_search[0] != element_to_find:
        return None

    # Check left half of list    
    if arr_to_search[median] > element_to_find:
        return binary_search(arr_to_search[:median], element_to_find)
    # Check right half of list
    elif arr_to_search[median] < element_to_find:
        return binary_search(arr_to_search[median:], element_to_find)

l = sorted([12, 11, 13, 5, 6, 7, -1])
print binary_search(l, 5)
print binary_search(l, 0)

l = sorted(['F', 'C', 'A', 'Z', 'W'])
print binary_search(l, 'A')
print binary_search(l, 'Y')
