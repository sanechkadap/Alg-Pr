import math
from math import cos,sin

# 1)
k = int(input("k:"))
A = pow(100,3)-pow(92,2)+k
print(A)

# 2)
x = int(input("x:"))
B = math.sqrt((1-math.cos(x))/2)
print(B)

# 3)
x2 = int(input("x2:"))
C = (math.sqrt(math.fabs(x2))*math.log(10, math.pow(x2, 2)))/(-5/4*x2+math.pow(math.e, x2/2))
print(C)

# 4)
x3 = int(input("x3:"))
y = int(input("y:"))
D = math.sqrt(math.pow(math.sin(x3),2)+math.pow(math.cos(math.pow(y),3),2)
print(D)

# 5)
x4 = int(input("x4:"))
y2 = int(input("y2:"))
E = math.sqrt(x4+math.sqrt(math.pow(x4,2)+4*math.pow(y2,2)))
print(E)

# 6)
x5 = int(input("x5:"))
a2 = int(input("a2:"))
F = math.pow(math.e,-1/2)*(x5-a)
print(F)

# 7)
x6 = int(input("x6:"))
G = 1/math.tan(x6)-math.sin(math.sqrt(pow(x6,2)+1))
print(G)

# 8)
a3 = int(input("a3:"))
b2 = int(input("b2:"))
c2 = int(input("c2:"))
d2 = int(input("d2:"))
n2 = int(input("n2:"))
H = math.log(b2,10)/(c2-d2)
J = math.pow(10,n2+3)
I = 1/8-math.fabs(b2)/(J+H)
K2 = 0.25*(a3-b2)/I
print(K2)
