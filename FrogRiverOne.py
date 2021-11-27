# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(x, arr):
    # creating the steps the frog should make
    steps = set([i for i in range(1, x + 1)])
    # creating the steps the frog already did
    froggy_steps = set()

    for index, leaf in enumerate(arr):
        if leaf <= x:
            froggy_steps.add(leaf)
        if froggy_steps == steps:
            return index
    return -1


def solution(X, A):
    # write your code in Python 3.6
    
    my_set = set()
    
    for value in range(1, X+1):
        my_set.add( value )

    for index in range(0, len(A) ):
        if A[index] in my_set:
            my_set.remove( A[index] )
        if my_set == set():
            return index
    
    return -1
