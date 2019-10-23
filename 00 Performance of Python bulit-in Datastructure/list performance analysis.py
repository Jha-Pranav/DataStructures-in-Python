from timeit import Timer
# concatination method
def test1():
    l = []
    for i in range(10000):
        l = l + [i]
    return l

# Append method
def test2():
    l = [] 
    for i in range(10000):
        l.append(i)

    return l

# List Comprehension
def test3():
    return [i for i in range(10000)]

# Using list function
def test4():
    return list(range(10000))

def dummyfunction():
    pass


t = Timer('dummyfunction()', 'from __main__ import dummyfunction')
t = t.timeit(100)
print("Function call takes ", t, ' miliseconds')


t1 = Timer('test1()', 'from __main__ import test1')
print("Concatination : ", t1.timeit(100) - t)

t2 = Timer('test2()', 'from __main__ import test2')
print("Append : ", t2.timeit(100) - t)

t3 = Timer('test3()', 'from __main__ import test3')
print("List comprehension  : ", t3.timeit(100) - t)

t4 = Timer('test4()', 'from __main__ import test4')
print("Range method : ", t4.timeit(100) - t)
