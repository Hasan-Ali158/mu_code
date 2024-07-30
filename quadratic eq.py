import math

a=float(input('Enter the value of a:'))
b=float(input('Enter the value of b:'))
c=float(input('Enter the value of c:'))

disc = b**2-4*a*c

if a==0:
    root=-c/b
    print('The eq has linear and only one root:', {root})

elif disc<0:
    print('Roots of eq are imaginary:')

else:
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)


