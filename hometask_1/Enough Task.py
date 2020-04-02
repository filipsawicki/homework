"""
Given a list lst and a number N, create a new list that contains each number of lst at most N times without
reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3].

"""
from collections import Counter

def delete_nth(order,max_e):
    """ temporary list"""
    temp = []
    for i in (order):
        if temp.count(i) < max_e:
            temp.append(i)
    print(temp)



delete_nth([20,37,20,21], 1)

delete_nth([1,1,3,3,7,2,2,2,2], 3)