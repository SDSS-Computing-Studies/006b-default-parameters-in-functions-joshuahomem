#! python3

import math

def tempconversion(a,b="C"):
    if b=="C":
        tempF=(a*1.8)+32
        return tempF
    elif b=="F":
        tempC= (a-32)*0.556
        return tempC


def factorPair(a,b):
    if a>b:
        num1=a/b
        myanswer=[num1,b]
        myanswer.sort()
        return myanswer
    elif b>a:
        num2=b/a
        myanswer=[int(num2),int(a)]
        myanswer.sort(int(num2),int(a))
        print(myanswer)
        return myanswer


def cosineLaw(a,b,c,oppositeSide=True):

    if oppositeSide==True:
        
        num1= math.sqrt((a**2) + (b**2) - (2*a*b*math.cos(toRadians(c))))
        return num1
    if oppositeSide==False:
        # a = opposite side
        # b = short side
        # c = angle
        if a>b:
            c=toRadians(c)
            coeff1= 1
            coeff2=-2*b*(math.cos(c))
            coeff3=(b**2)-(a**2)
            coeff1=float(coeff1)
            coeff2=float(coeff2)
            coeff3=float(coeff3)
            solution=[]
            solution=quadratic(coeff1,coeff2,coeff3)
            print(solution)
            solution.sort()
            sol=solution[1]
            return sol
        elif b>a:
            c=toRadians(c)
            coeff1= 1
            coeff2=-2*a*(math.cos(c))
            coeff3=(a**2)-(b**2)
            coeff1=float(coeff1)
            coeff2=float(coeff2)
            coeff3=float(coeff3)
            solution=[]
            solution=quadratic(coeff1,coeff2,coeff3)
            solution.sort()
            sol=solution[1]
            return sol
        """solution1=(-1*coeff2 + (math.sqrt((coeff2**2) - (4 * coeff1 * coeff3))))/(2*coeff1)
        solution2=(-1*coeff2 - (math.sqrt((coeff2**2) - (4 * coeff1 * coeff3))))/(2*coeff1)
        solution1=float(solution1)
        solution2=float(solution2)
        print(solution1,solution2)
        if solution1>0:
            return solution1
        elif solution2>0:
            return solution2

    """


def toRadians(c):
    radians=(c*math.pi)/180
    return radians
    
def solution(a):
    a.sort()
    answer=a[1]
    return answer

def quadratic(a,b,c):
    disc=(b**2)-(4*a*c)
    
    if disc==0:
        quadratics=1
    elif disc>0:
        quadratics=2
    if quadratics==2:
        solutions1=((-1*b) + math.sqrt((b**2) - 4 * a * c))/(2*a)
        solutions2=((-1*b) - math.sqrt((b**2) - 4 * a * c)) /(2*a)
        solutions=[]
        solutions.append(solutions1)
        solutions.append(solutions2)
        solutions.sort()

        return solutions
    elif quadratics==0:
        solutions=[]
        solutions1=((-1*b)+ math.sqrt((b**2) - 4 * a * c))/(2*a)
        solutions2=((-1*b)- math.sqrt((b**2) - 4 * a * c)) /(2*a)
        solutions.append(solutions1)
        solutions.append(solutions2)
        solutions.sort()
        return solutions



