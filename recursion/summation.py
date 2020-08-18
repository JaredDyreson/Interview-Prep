#!/usr/bin/env python3.8

import random

def redo(container):
    if(len(container) == 0):
        return 0
    else:
        return container[0] + redo(container[1:])

def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:]) 

def summation(container: list, x: int) -> int:
    if(x >= len(container)):
        return 0
    return container[x] + summation(container, x+1)

print(summation([1, 2, 3], 0))
# def test():
    # for x in range(0, 100):
        # container = [random.randint(0, 10) for x in range(10)]
        # if(summation(container, 0) != sum(container)):
            # print(f'failed at index {x} with container of {container}')
            # quit()
    # print("all tests passed!")
# test()
