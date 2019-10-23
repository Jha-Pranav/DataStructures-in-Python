from random import randint

def merge(lst1,lst2):
    """
    This function is used to merge two sorted list
    """
    result = []
    i = 0
    j = 0
    while i<len(lst1) and j<len(lst2): # This loop will exhaust on of the list having min val.
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    while i< len(lst1): # This will just append all the remaining items in lst1
        result.append(lst1[i])
        i += 1

    while j < len(lst2): # This will just append all the remaining items in lst2
        result.append(lst2[j])
        j += 1

    return result


def merge_sort(nums):
    if len(nums) == 1 :
        return nums
    midPoint = len(nums)//2

    left = merge_sort(nums[:midPoint])
    right = merge_sort(nums[midPoint:])
    return merge(left,right)
    

a_list = [randint(10,j) for j in range(100,600)]
print(merge_sort(a_list))


