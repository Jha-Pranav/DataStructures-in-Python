def sequentialSearch(obj, item):
    for p,i in enumerate(obj):
        if i == item:
            return True,p
    return False


print(sequentialSearch([1,2,3,4,55,6,77,34,78,98],55))
