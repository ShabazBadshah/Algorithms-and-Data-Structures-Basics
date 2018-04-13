from collections import deque
import random

'''
Rotates a list left amount_rot times

0 <= amount_rot <= len(arr) - 1

Worst Case Runtime: O(n)
Space: O(1)
'''
def left_rotate_normal(arr, amount_rot):
    left_rot_arr = []

    for i in range (amount_rot, len(arr)):
        left_rot_arr.append(arr[i])

    for i in range (0, amount_rot):
        left_rot_arr.append(arr[i])

    return left_rot_arr


'''
Worst Case Runtime: O(n + n) = O(2n) = O(n)
Space: O(n)
'''
def left_rotate_queue(arr, amount_rot):
    lstQueue = deque()

    for val in arr:
        lstQueue.append(val)

    for i in range (amount_rot):
        temp = lstQueue.popleft()
        lstQueue.append(temp)

    return lstQueue


arr = random.sample(range(1, 10), 9)

print("\nLeft Rotate Normal\n------------------")
print ("Rotate Left 2:  " + str(left_rotate_normal(arr, 2)))
print ("Rotate Left 3:  " + str(left_rotate_normal(arr, 3)))
print ("Rotate Left 10: " + str(left_rotate_normal(arr, 9)))
print("\nLeft Rotate with Queue\n----------------------")
print ("Rotate Left 2:  " + str(left_rotate_normal(arr, 2)))
print ("Rotate Left 3:  " + str(left_rotate_normal(arr, 3)))
print ("Rotate Left 10: " + str(left_rotate_normal(arr, 9)))
# print (list(left_rotate_queue(arr, 2)))