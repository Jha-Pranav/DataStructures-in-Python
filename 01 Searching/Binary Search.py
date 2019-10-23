#  Binary search follows a divide and conquer methodology.
#  It is faster than linear search but requires that the array 
#  be sorted before the algorithm is executed.

def binarySearch(a_list,val):
    start = 0
    end = len(a_list) - 1
    
    mid = (start + end)//2 # double division floor the result
    while a_list[mid] != val and start <= end :
        # either query element should be equal or we reached at the same point.
        if val > a_list[mid] :
            start = mid + 1  # floor operation reduce it's chance to reach at extrime end.
            # eg :  a_list having size 100 and suppose you are trying to search element at 100th postion
            # means 98+99//2 will always return 98 we never reach at 99th index. 
            
        elif val < a_list[mid] :
            end = mid - 1

        mid = (start + end) // 2
            

    if a_list[mid] == val:  # Inorder to check values at the boundaries 
        return True
    else:
        return False


a_list = [i for i in range(100)]

print(binarySearch(a_list,0))
