# for this exercise it is necessary to know the condition of existence of the triangle

# s1, s2 and s3 are the sides of the triangle
s1 = float(input('Enter the first value of the triangle: '))
s2 = float(input('Enter the second value of the triangle: '))
s3 = float(input('Enter the third value of the triangle: '))

# checking if values can form a triangle
if abs(s1-s2) < s3 and s3 < (s1+s2):
    if abs(s1-s3) < s2 and s2 < (s1+s3):
        if abs(s2-s3) < s1 and s1 < (s2+s3):
            # if true, classify the triangle
            if s1 == s2 and s1 == s3:
                print('Equilateral triangle.')
            else:
                if (s1 == s2) or (s1 == s3) or (s2 == s3):
                    print('Isosceles triangle.')
                else:
                    print('Scalene triangle.')
