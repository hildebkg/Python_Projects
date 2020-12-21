#Law of Cosines Calculator 
#(When you know two side lengths and the angle between them)

import math

a = float(input('Enter side length a '))
b = float(input('Enter side length b '))
C1 = float(input('Enter the angle between sides a and b in degrees '))

C2 = C1*(math.pi/180)

if a < 0 or b < 0 or C1 < 0 or C1 > 180:
    if a < 0:
        print('Side a is invalid')
    else:
        print('Side a is valid')
    if b < 0:
        print('Side b is invalid')
    else:
        print('Side b is valid')
    if C1 < 0 or C1 > 180:
        print('Angle C is invalid')
    else:
        print('Angle C is valid')
    
else:
    c = math.sqrt((a**2)+(b**2)-(2*a*b*(math.cos(C2))))
    print('The third side length is {0:.5f}\n'.format(c))

