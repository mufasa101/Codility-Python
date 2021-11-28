def solution(arr):
    if len(arr)<0:
        return 0
    arr.sort()
    i=0
    for item in range(1,len(arr)+1):
        if item!=arr[i]:
            return 0
        i+=1
    return 1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    sorted_array = sorted(A)

    expected_num = 1
    for item in sorted_array:
        if item == expected_num:
            expected_num += 1
        else:
            return 0

    return 1
