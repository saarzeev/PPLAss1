from ComplexNum import *

class X:
    def __init__(self):
        pass

class R():
    def __init__(self):
        pass

class Y(X,R):
    def __init__(self):
        X.__init__(self)

class Z(Y):
    def __init__(self):
        X.__init__(self)

class T():
    def __init__(self):
        X.__init__(self)


x = X()
y = Y()
z = Z()
r = R()


print("Check isInstancePPL")
print(isInstancePPL(x, X)) #True
print(isInstancePPL(x, Y)) #False
print(isInstancePPL(y, X)) #True
print(isInstancePPL(y, Y)) #True
print(isInstancePPL(r, X)) #False
print(isInstancePPL(x, R)) #False
print(isInstancePPL(y, R)) #True
print("Check isSubclassPPL Regular")
print(isSubclassPPL(X, X)) #True
print(isSubclassPPL(X, Y)) #False
print(isSubclassPPL(Y, X)) #True
print(isSubclassPPL(Y, Y)) #True
print("Check isSubclassPPL type")
print(isSubclassPPL(type(x), X)) #True
print(isSubclassPPL(type(x), Y)) #False
print(isSubclassPPL(type(y), X)) #True
print(isSubclassPPL(type(y), Y)) #True
print("Check isSubclassPPL Class")
print(isSubclassPPL(x.__class__, X)) #True
print(isSubclassPPL(x.__class__, Y)) #False
print(isSubclassPPL(y.__class__, X)) #True
print(isSubclassPPL(y.__class__, Y)) #True
print("Check numInstancePPL")
print(numInstancePPL(x, X)) #1
print(numInstancePPL(x, Y)) #0
print(numInstancePPL(y, X)) #2
print(numInstancePPL(y, Y)) #1
print(numInstancePPL(r, X)) #0
print(numInstancePPL(x, R)) #0
print(numInstancePPL(y, R)) #2
print(numInstancePPL(z, X)) #3
print(numInstancePPL(z, R)) #3
print(numInstancePPL(z, Y)) #2
print(numInstancePPL(z, Z)) #1
print(numInstancePPL(z, T)) #0
print("Check numSubclassPPL")
print(numSubclassPPL(Y, X)) #2
print(numSubclassPPL(Y, Y)) #1