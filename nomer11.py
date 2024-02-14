import math

R = int(input("R:"))
a = int(input("a:"))
b = math.sqrt(2*math.pow(R,2)-2*R*math.sqrt(math.pow(R,2)-(math.pow(a,2)/4)))
print(b)
