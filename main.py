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

print ("is callable %s" %callable(lambda x: x > 2))
print("Check count_if")
print(count_if([1, 0, 8], lambda x: x > 2)) #1
print(count_if([1, 1, 8], lambda x: x == 1)) #2

print("Check for_all")
print(for_all([1,0,8], lambda x: x*2, lambda x: x>0)) #False
print(for_all([1,1,8], lambda x: x, lambda x: x>0)) #True
#print(for_all([], lambda x: x, lambda x: x>0)) #Exception

print("Check for_all_red")
print(for_all_red([3], lambda x, y: x*y, lambda x: x>0)) #False
print(for_all_red ([1,1,8], lambda x, y: x*y, lambda x: x>7)) #True
#print(for_all_red ((1,1,8), lambda x: x, lambda x: x>7)) #Exception

print("Check there_exists")
print(there_exists([1, 0, 8],3, lambda x: x > 2)) #False
print(there_exists([1, 1, 8],2, lambda x: x == 1)) #True
print(there_exists([1, 1, 8],3, lambda x: x > 0 )) #True
print(there_exists([1, 1, 8],"3", lambda x: x + 1 )) #False


z = ComplexNum(1,2)

print(str(z))
print(z == ComplexNum(1,1))
print(z == ComplexNum(1,2))
print(z + ComplexNum(1,-3))
print(-z)
print(z-ComplexNum(4,3))
print(z*z)
print(str(z * ComplexNum(2, 3)))
try:
   print(str(z * 2))
except:
    print("")
print(str(z.conjugate()))
print(str(z.abs()))
