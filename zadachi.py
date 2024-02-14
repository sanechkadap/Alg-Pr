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
import math

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
if x<z:
    min = x 
    max = z
else: 
    min = z 
    max = x 
if y<max:
    min = y 
L = 2*max-3*min 
print(L)
######################6
import math

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a<b:
    min = a 
    max = b
else: 
    min = b 
    max = a 
if c>max:
    max = c
else:
    min = c 
P = (max+min)/2
print(P)
######################7
import math

a = int(input("a:"))
b = int(input("b:"))

if a%2==0:
    print("число A четное")
else:
    print("число А нечетное")
if b%2==0:
    print("число B четное")
else:
    print("чило В нечетное")
if a%2==0 and b%2==0:
    print("оба числа четные")
elif a%2!=0 and b%2!=0:
    print("оба числа нечетные")
        
