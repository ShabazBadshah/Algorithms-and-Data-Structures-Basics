import random
import time

'''
Runtime Worst Case: infinite 
Runtime Avg Case: O(n*n!) = O(n!)
Runtime Best Case: O(n)
Space: O(1)
'''

'''
Bogosort is not a sorting algorithm used by anyone, anywhere. It's more of a joke than an actual
sorting algorithm. Bogosort will take an array and randomize it to sort it. It will keep
randomizing the array until it comes back sorted.
'''
def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            return False
    return True

print ("Running Bogosort 5 times on the same list\n")
i = 0
while (i < 5):
    arr = random.sample(range(1, 19), 9)
    random.shuffle(arr)

    start_time = time.time()
    sorted_arr = bogosort(arr)
    end_time = time.time()

    elapsed_time = round(end_time - start_time, 3)
    print (sorted_arr)
    print ("Time to sort list: " + str(elapsed_time) + " seconds\n")

    i += 1