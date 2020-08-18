#!/usr/bin/env python3.8

import random

def qs(container: list, left: int, right: int):
    if(left >= right):
        return
    pivot = container[int((left + right)/2)]
    index = partition(container, left, right, pivot)
    qs(container, left, index - 1)
    qs(container, index, right)

def partition(container: list, left: int, right: int, pivot: int):
    while(left <= right):
        while(container[left] < pivot):
            left+=1
        while(container[right] > pivot):
            right-=1
        if(left <= right):
            container[left], container[right] = container[right], container[left]
            left+=1
            right-=1
    return left

def func(container: list):
    qs(container, 0, len(container)-1)

def test():
    example = [random.randint(0, 1000) for x in range(0, 100)]
    example_copy = example
    func(example)
    return (example == sorted(example_copy))

for x in range(0, 1000):
    if not(test()):
        print(f'failed at test {x}')
        quit()
print("finished all tests!")

