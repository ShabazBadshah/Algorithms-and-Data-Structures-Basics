import random
import time

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