import math

opp = float(input('Insert the value of opposite side of the right triangle: '))
adj = float(input('Insert the value of adjacent side of the right triangle: '))

hip = math.hypot(opp,adj)

print(f'The value of hypotenuse is: {hip}')
