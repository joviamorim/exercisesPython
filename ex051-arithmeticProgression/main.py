firstTerm = int(input('Enter the first term of the arithmetic progression: '))
reason = int(input('Enter the reason of arithmetic progression: '))

# ap = arithmetic progression
ap = firstTerm
for i in range(0,10):
    print(ap)
    ap = reason + ap
