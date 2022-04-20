# fTerm = first term of the arithmetic progression
fTerm = int(input('Enter the first term of the arithmetic progresion: '))
reason = int(input('Enter the reason: '))

ap = fTerm # ap = initial value of arithmetic progression
qTerm = 0 # qterm = quantity of terms on ap

while qTerm <= 10:
    print(ap)
    ap = ap + reason   
    qTerm += 1
