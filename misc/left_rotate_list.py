from collections import deque

def left_rotate_normal(arr, amount_rot):
    left_rot_arr = []

    for i in range (amount_rot, len(arr)):
        left_rot_arr.append(arr[i])

    for i in range (0, amount_rot):
        left_rot_arr.append(arr[i])

    return left_rot_arr


def left_rotate_queue(arr, amount_rot):
    lstQueue = deque()

    for val in arr:
        lstQueue.append(val)

    for i in range (amount_rot):
        temp = lstQueue.popleft()
        lstQueue.append(temp)

    return lstQueue


arr = [1, 2, 3, 4, 5]
print (left_rotate_normal(arr, 2))
print (list(left_rotate_queue(arr, 2)))