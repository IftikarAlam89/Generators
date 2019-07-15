"""
Module for trying out generator execution
"""

def take(count,iterable):
    """
    Take items from the front of an iterable

    :param count:The maximum number of items to retreive
    :param iterable:The source series

    :return:At most 'count' objects from iterable
    """

    counter =0
    for item in iterable:
        if counter == count:
            return
        counter+=1
        yield item

def distinct(iterable):
    """
    Return unique elements in set by removing distinct elements

    :param
    iterable:  the series of elements

    :Yields:
    Series of elements in order wothout duplicates

    """

    seen=set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items=[5,7,7,6,5,4,3,3,2]
    for item in distinct(items):
        print(item)


def run_take():
    items=[1,3,4,5,9,11]
    for item in take(3,items):
        print(item)

def run_pipeline():
    items=[2,2,2,2,2,2,3,3,3,3,5,6,6,7,7,8]
    for item in take(3,distinct(items)):
        print(item)

from math import sqrt

def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

if __name__=='__main__':
    run_pipeline()

