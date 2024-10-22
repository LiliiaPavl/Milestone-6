eq = '4*x**2 +4*x +    (-8) =  0'
res = eq.replace(" ", "").replace("(","").replace(")","")
print(res)
a = int(res.split('*x**2+')[0])
print(a)
b = int(res.split('*x**2+')[1].split('*x+')[0])
print(b)
c = int(res.split('*x+')[1].split('=')[0])
print(c)
import math
x1 = (-b + math.sqrt(discriminant)) / (2*a)
x2 = (-b - math.sqrt(discriminant)) / (2*a)
print(x1,x2)