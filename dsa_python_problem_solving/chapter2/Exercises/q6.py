'''
Devise an experiment to verify that the list index operator is O(1)
'''

from timeit import Timer

def test1():
    l = [1,2,3]
    return l.index(2)


def test2():
    l = [1,2,3,4,5,6,7,8,9]
    return l.index(5)

def test3():
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]
    return l.index(13)

t1 = Timer("test1()", "from __main__ import test1")
print(f"test1: {t1.timeit(number=1000):15.2f} milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print(f"test2: {t2.timeit(number=1000):19.2f} milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print(f"test3: {t3.timeit(number=1000):10.2f} milliseconds")

# we see that there is constant time -> 0 milliseconds
# regardless of list size or which element is to be accessed
# thus, O(1)