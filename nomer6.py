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
