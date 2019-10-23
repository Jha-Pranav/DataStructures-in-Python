def bubble_sort(a_list):
    """"
    iterates over a list, comparing elements in pairs and swapping them until
     the larger elements "bubble up" to the end of the list,
     and the smaller elements stay at the "bottom".
    """

    swapped = True  # for first execution of while loop
    while swapped : 
        swapped = False
        for i in range(len(a_list)-1):
            if a_list[i] > a_list[i+1]:
                #Swapping two number
                a_list[i], a_list[i+1] = a_list[i+1],a_list[i]
                #setting it flag to True
                swapped = True
    return a_list



import random

a_list = [random.randint(100,j) for j in range(900,950)]
print(a_list)
print(bubble_sort(a_list))
