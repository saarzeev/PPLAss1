import math
from functools import reduce
from inspect import signature

class ComplexNum:
    def __init__(self, re, im=0):
        self.re = re
        self.im = im

        if im < 0:
            self._im_sign = "-"
        else:
            self._im_sign = "+"

    def re(self):
        return self.re

    def im(self):
        return self.im

    def to_tuple(self):
        return (self.re, self.im)

    def __repr__(self):
        return str(self.re) + " " + self._im_sign + " " + str(abs(self.im)) + "i"

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(other)

        if isinstance(other, ComplexNum):
            return self.im == other.im and self.re == other.re
        else:
            return False

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(other)

        if isinstance(other, ComplexNum):
            return ComplexNum(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return ComplexNum(- self.re, - self.im)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(other)

        if isinstance(other, ComplexNum):
            return self + (-other)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(other)

        if isinstance(other, ComplexNum):
            return (-self) + other

    def __mul__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError("Complex multiplication only defined for Complex Numbers.")

        # (x + yi)(u + vi) = (xu – yv) + (xv + yu)i
        return ComplexNum(self.re * other.re() - self.im * other.im, self.re * other.im + self.im * other.re)

    def conjugate(self):
        return ComplexNum(self.re, -self.im)

    def abs(self):
        return math.sqrt(self*self.conjugate())


def isInstancePPL(object1, classInfo):
    return isSubclassPPL(type(object1), classInfo)


def numInstancePPL(object1, classInfo):
    return numSubclassPPL(type(object1), classInfo)


def isSubclassPPL(class1, classInfo):
    return classInfo in class1.mro()

def numSubclassPPL(class1, classInfo):
    ancestors_list = class1.mro()
    if classInfo in ancestors_list:
        return ancestors_list.index(classInfo) + 1
    return 0


def is_iterable(obj):
    try:
        lst = iter(obj)
    except TypeError as e:
        return False
    return True

def count_if(lst,func):
    if (not is_iterable(lst) or len(lst) < 1):
        raise Exception("lst must be non emptry iterrable object")
    if (not callable(func) or len(signature(func).parameters) != 1):
        raise Exception("func must be a function with 1 parameters")
    return len(list(filter(func,lst)))

def for_all(lst,func1,func2):
    if (not is_iterable(lst) or len(lst) < 1):
        raise Exception("lst must be non emptry iterrable object")
    if (not callable(func1) or len(signature(func1).parameters) != 1):
        raise Exception("func1 must be a function with 1 parameters")
    if (not callable(func2) or len(signature(func2).parameters) != 1):
        raise Exception("func2 must be a function with 1 parameters")
    return reduce(lambda x,y : x and y,map(func2,list(map(func1,lst))))

def for_all_red(lst,func1,func2):
    if (not is_iterable(lst) or len(lst) < 1):
        raise Exception("lst must be non emptry iterrable object")
    if (not callable(func1) or len(signature(func1).parameters) != 2):
        raise Exception("func1 must be a function with 2 parameters")
    if (not callable(func2) or len(signature(func2).parameters) != 1):
        raise Exception("func2 must be a function with 1 parameters")
    return func2(reduce(func1,lst))

def there_exists(lst,n,func1):
    return count_if(lst,func1) == n