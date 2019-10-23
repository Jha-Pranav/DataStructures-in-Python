from random import randint

def insertion_sort(nums):
    
    for i in range(1,len(nums)):
        for j in range(i-1,-1,-1): # A loop starting with the last sorted item towards beginning.
            if nums[i]<nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
                i -= 1 # Next comparision will be with the swapped item towards sorted list
    return nums

# a_list = [29,10,14,37,14]
a_list = [randint(0,j) for j in range(400,500)]
print(insertion_sort(a_list))