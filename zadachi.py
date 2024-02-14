#####################1
import math

N = int(input("N:"))
if N%3== 0:
    print("delitsa")
else:
    print("ne delitsa")
  ###################2
  import math
x = int(input("x:"))
y = int(input("y:"))
if x < y:
    min = x
    max = y
else: 
    min = y
    max = x
z = (min+0.5)/(1+math.pow(max,2))
print(z)
#######################3
import math 
x = int(input("x:"))
y = int(input("y:"))

if x<y:
        min = x
        max = y
    else:
        min = y
        max = x

if x < 0:
    z = max
else: 
    z = min
#######################4
import math

x = int(input("x:"))
y = int(input("y:"))
if x<y:
    min = x
else:
    min = y
if x<y:
    max = y**2
else:
    max = x**2
if y<0:
    z = max
else:
    z = min
print(z)
######################5
