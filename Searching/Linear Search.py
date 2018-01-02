'''
Returns the element if found, otherwise
return None

Runtime: O(n)
Space: O(1)
'''
def linear_search(arr_to_search, element_to_find):
    for i in range(len(l)):
        if l[i] == element_to_find and type(l[i]) == type(element_to_find):
            return l[i]
    return None

l = [12, 11, 13, 5, 6, 7, -1]
print linear_search(l, 12)
print linear_search(l, -2)
print linear_search(l, 7)
