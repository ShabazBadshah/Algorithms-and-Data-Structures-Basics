'''
Given a list of numbers find the most frequently occuring number

Worst Case Runtime: O(n)
'''
def most_frequent(arr):
    
    if arr == []:
        return 'Cannot find the most frequent number in an empty array'

    arr_hashtable = {}

    for num in arr:
        if num not in arr_hashtable:
            arr_hashtable[num] = 1
        else:
            arr_hashtable[num] += 1

    most_freq_num = max(arr_hashtable.values())

    for key in arr_hashtable.keys():
        if arr_hashtable[key] == most_freq_num:
            return key

    return 'Most frequent number does not exist'

arr = [1, 4, 5, 8, 9, 0, 1, 3, 1, 1, 1, 6, 4, 5, 7]
print (most_frequent(arr))

arr = [1, 4, 6, 4, 5, 7]
print (most_frequent(arr))

arr = [9]
print (most_frequent(arr))

arr = []
print (most_frequent(arr))