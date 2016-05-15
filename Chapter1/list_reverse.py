#!/usr/bin/env python
#encoding=utf-8

from time import *

def reverse1(count):

    start_time = time()

    nums=[]
    for i in range(count):
        nums.append(i)  #并不需要移动,直接增加元素

    nums.reverse()  #只需要移动一次

    use_time = time() - start_time

    print use_time


def reverse2(count):

    start_time = time()

    nums = []
    for i in range(count):
        nums.insert(0, i)  #这里插入到列表的头部，每一个操作都需要进行移位操作，后面所有的元素都需要往后移动一位

    use_time = time() - start_time

    print use_time


count = 10**6
reverse1(count)
reverse2(count)

'''
count = 10**5

0.00971913337708
2.41431879997

count = 10*6
0.0991959571838
257.013590097

'''

