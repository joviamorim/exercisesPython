s1 = float(input('Enter the first score: '))
s2 = float(input('Enter the second score: '))

mean = (s1 + s2) / 2

if mean < 5.00:
    print(f'{mean}. Reproved')
elif mean == 5.00 and mean < 7.00:
    print(f'{mean}. Take the recovery test')
else:
    print(f'{mean}. Approved')
