import math
n = -100
while (3*n*math.pow(n, 4)-730*n<5):
    n+=1
print(n)
##############################
import math
n = 2
while (math.pow(math.e ,n) - 1000 * math.log(10,n)<=10):
    n+=1
print(n)
#################################
import math
m = int(input(("Введи число: ")))
k = 1
while pow(4 , k) < m :
    k+=1
    print(k)
###############################

import math
n = int(input("Введите число: "))
r = 0
while math.pow(2,r)<=n:
    r += 1
print("число R", r)
#################################
import math
i = 1
e = math.pow(10,-4)
while abs(((2*i)**2)/((2*i-1)*(2*i+1))-1)>e:
    i+=1
    x = ((2*i)**2)/((2*i-1)*(2*i+1))
    print(x)
##################################
