import random

'''
Given a list of numbers from 1 to 100 (in any order) there is one duplicate in the list
and the function below will find it

Worst Case Runtime: O(n)
'''
def duplicate_occurrence(arr):
    
    arr_hashtable = {}

    for num in arr:
        if num not in arr_hashtable:
            arr_hashtable[num] = 1
        else:
            return num
        
    return 'Duplicate element was not found'

'''
Generate a random list of numbers between 1 and 100 and insert a duplicate 
into the list
'''
arr = random.sample(range(1, 100), 99)
duplicate_num = random.choice(arr)
arr.append(duplicate_num)
random.shuffle(arr)

ret_dup_occurrence = duplicate_occurrence(arr)
print ("The duplicate number was: " + str(duplicate_num))
print ("Duplicate numbers match: " + str(ret_dup_occurrence == duplicate_num))