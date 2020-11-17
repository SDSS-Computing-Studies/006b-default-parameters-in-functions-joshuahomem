#!python3
import assignment
import math

a=10
b=3
c=50

coeff1= 1
coeff2=-2*a*(math.cos(assignment.toRadians(c))) 
coeff3=  a**2 - b**2
coeff2 = float(coeff2)
coeff1 = float(coeff1)
coeff3 = float(coeff3)

a = coeff1
b = coeff2
c = coeff3
print(a,b,c)
print(-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)
print(-1*b - math.sqrt(b**2 - 4*a*c))/(2*a)
exit()
solution1=(-1*coeff2 + math.sqrt(coeff2**2 - 4 * coeff1 * coeff3))/(2*coeff1)
solution2=(-1*coeff2 - (math.sqrt((coeff2**2) - (4 * coeff1 * coeff3))))/(2*coeff1)
solution1=float(solution1)
solution2=float(solution2)

print (solution1)
print(solution2)
"""
quad=(coeff2**2) - (4 * coeff1 * coeff3)
quad=float(quad)
quade=math.sqrt(quad)
quade=float(quade)
quad1=(-1*coeff2)-quade       
quad2=(-1*coeff2)+quade 
quad1=float(quad1)
quad2=float(quad2)

sol1=quad1/(2*coeff1)
sol2=quad2/(2*coeff1)

print(sol1)

print(sol2)
"""