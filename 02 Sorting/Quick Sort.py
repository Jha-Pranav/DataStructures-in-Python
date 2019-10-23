def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums.pop()
    smaller_list = []
    larger_list = []
    for i in nums:
        if pivot > i:
            smaller_list.append(i)
        else:
            larger_list.append(i)

    return quick_sort(smaller_list)+ [pivot] + quick_sort(larger_list)


lst1 = [29,10,14,37,14]
print(quick_sort(lst1))

