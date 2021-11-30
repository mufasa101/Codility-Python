def solution(arr):

    if len(arr)<1:
        return 0
    min_data=arr[0]
    max_profit=0
    sum_cum=0
    for i in range(1,len(arr)):
        if arr[i] <  min_data:
            min_data=arr[i]
            # print("new_lessssssssssss",min_data)
            sum_cum=0
        else:
            profit_made=(arr[i]-arr[i-1])
            
            print("profit",profit_made)
            sum_cum+=profit_made
            if max_profit < sum_cum:
                max_profit=sum_cum
            print("new cumm:",sum_cum)
            print("max_profit:",max_profit)

        # if arr[i] >max_data:
        #     max_data=arr[i]
    # print("max=",max_data,"min=",min_data)
    return max_profit


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # key point: try to use only one for-loop O(n)
    
    if len(A)==0:
        return 0
    
    max_profit = 0
    min_price = A[0]
    
    for item in A:
        max_profit = max( max_profit, item - min_price )
        min_price = min( min_price, item )

    return max_profit
