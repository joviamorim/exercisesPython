# fTerm = first term of the arithmetic progression
fTerm = int(input('Enter the first term of the arithmetic progresion: '))
reason = int(input('Enter the reason: '))

ap = fTerm # ap = initial value of arithmetic progression
qTerm = 10 # qterm = quantity of terms on ap

while qTerm > 0:
    while qTerm > 0:
        print(ap)
        ap = ap + reason   
        qTerm -= 1
    
    qTerm = int(input('Enter the quantity of additional terms you want to see (If you want to exit, enter 0): '))
