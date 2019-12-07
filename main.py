from ComplexNum import *

class A:
    pass

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

print(isInstancePPL(a, A))
print(isInstancePPL(b, A))
print(isInstancePPL(a, B))
print(isInstancePPL(a, a))


print(numInstancePPL(a, A))
print(numInstancePPL(b, A))
print(numInstancePPL(c, B))
print(numInstancePPL(a, B))
print(numInstancePPL(a, a))

print(isSubclassPPL(A, B))
print(isSubclassPPL(B, A))