
def solution(A):
    # write your code in Python 3.6
    if len(A)<3:
        return 0
    A.sort()
    for i in range(0,len(A)-2):
        if (A[i]+A[i+1]) > A[i+2]:
            return 1
    return 0

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # key point: sort the array 
    sorted_array = sorted(A)
    
    for index in range( len(A)-2 ):
        if sorted_array[index] + sorted_array[index+1] > sorted_array[index+2]:
            return 1
    
    return 0
