# for this exercise it is necessary to know the condition of existence of the triangle

side1 = float(input('Enter the first value of the triangle: '))
side2 = float(input('Enter the second value of the triangle: '))
side3 = float(input('Enter the third value of the triangle: '))

if abs(side1-side2) < side3 and side3 < side1+side2:
    if abs(side1-side3) < side2 and side2 < side1+side3:
        if abs(side2-side3) < side1 and side1 < side2+side3:
            print('Is possible the creation of a triangle with this values')
else:
    print('Is not possible the creation of a triangle with this values')
