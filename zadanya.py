x0, y0 = map(int,input("Введите числа X0, Y0: ").split())
r = 1
R = 2
tochka = ((x0**2)+(y0**2))**0.5
if r <= tochka <= R:
    print("tochka находится на кольце")
else:
    print("точка находится не на кольце")
###################################
x, y = map(int,input("Введите числа: ").split())
if x>0 and y<0:
    print("точка в правой нижней четверти")
elif x<0 and y>0:
    print("точка в левой верхней четверти")
elif x>0 and y>0:
    print("точка в правой верхней четверти")
elif x<0 and y<0:
    print("точка в левой нижней четверти")
####################################
x, y, R = map(int,input("Введите числа x, y, R: ").split())
if y < 0:
    a = R-(((x**2)+(y**2))**0.5)
else:
    a = ((x**2)+(y**2))**0.5
  ###################################
  x, y = map(int,input("Введите числа: ").split())
if x and y > 0:
    print("точка над полуплоскостью")
  №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

a, b, c = map(int,input("Введите числа: ").split())
if a+b>=c and b+c>=a and c+a>=b:
    print("можно сделать треугольник")
    p = a+b+c
    P = p/2
    S = (P*(P-a)*(P-b)*(P-c))**0.5
    print("Периметр треугольника -", P, "Площадь треугольника -", S)
else:
    print("нельзя сделать треугольник")
####################################
