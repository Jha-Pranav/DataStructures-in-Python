from random import randint

def selction_sort(nums):
    for i in range(len(nums)-1):
        swapp = False
        smallest_indx = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[smallest_indx]:
                smallest_indx = j
                swapp = True
        if swapp:
            nums[i], nums[smallest_indx] = nums[smallest_indx], nums[i]
    return nums

a_list = [randint(100,i) for i in range(9000,9500)]
print(selction_sort(a_list))
