import math

def get_digit(num,i):
    return (abs(num) // (10**i)) % 10

def max_digit_len(lst):
    max_digit = max(lst)
    return math.floor(math.log10(abs(max_digit))) + 1

def radix_sort(lst):
    for pos in range(max_digit_len(lst)):
        # **    bucket = [[]] * 10  
        # **  Don't use this becoz each individual list is having refence to the same location
        # change in any of the list will effect the same change in other too. **

        bucket = [[] for i in range(10)]
        for val in lst:
            bucket[get_digit(val,pos)].append(val)
        lst = []
        for small_bucket in bucket:
            if small_bucket:
                while small_bucket != []:
                    lst.append(small_bucket.pop(0))
        
    return lst


lst = [36848, 47,368, 453, 657, 66, 47, 10, 21]
print(radix_sort(lst))

# Note : This sorting algo is applicable for non- negative numbers only.
