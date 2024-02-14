import math

R = int(input("R:"))
r = int(input("r:"))
h = int(input("h:"))
l = math.sqrt(math.pow(h,2)+(math.pow((R-r),2)))
v = (1/3)*math.pi(math.pow(R,2)+math.pow(r,2)+R*r)
s = math.pi*(R+r)*l+math.pi*math.pow(R,2)+math.pi*math.pow(r,2)
print(V,S)
