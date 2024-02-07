import math

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
C = 1+(math.pow(x,2)/2)+(math.pow(y,2)/4)
A = (math.sqrt(math.fabs(x-1))-math.fabs(math.pow(y,1/3)))/C
print(A)

B = x*[math.atan(z)+math.pow(math.e,-(x+3))]
print(B)

#2 
A2 = (3+math.pow(math.e,y-1))/(1+math.pow(x,2)*math.fabs(y-math.tan(z)))
print(A2)

B2 = (1+math.fabs(y-x))+(math.pow(y-x,2)/2)+(math.pow(math.fabs(y-x),3))/3
print(B2)
