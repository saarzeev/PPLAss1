import math

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

