import math

def max_digit_len(lst):    
    """
    Return the length of the maximum digit from the list.
    """
    maximum_digit= max(lst)
    return math.floor(math.log10(abs(maximum_digit))) + 1

def counting_sort(lst):
    """
    Sort and return new list without effecting original one
    """
    # Creating bucket of length of maxium possible digit.
    bucket = [0 for i in range(pow(10, max_digit_len(lst)))]
    # creating output list having same length as original one.
    output = [0 for i in range(len(lst))]

    for i in lst:        # Add occurance of entities into the bucket  
        bucket[i] += 1   
   
    for j in range(1, len(bucket)):  
        # Adding number of occurance of each item with the next one
        # which eventually provide us the position in the output list.
        bucket[j] += bucket[j-1]
    
    for k in lst: 
        # Adding original item to the output list corresponding to the bucket postion value.
        output[bucket[k]-1] = k
        bucket[k] -= 1
    return output


lst = [5686,7975,45745,4674,7890,790,7986,97,975,969,69,8,9790,43675,2,3,5,0,6,66,88,98]
print(counting_sort(lst))

# Note : This algo is currently not applicable for negative numbers
