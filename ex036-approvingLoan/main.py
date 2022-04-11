salary = float(input('Insert your salary: '))
loan = float(input('Insert the loan value: '))
months = int(input('Insert how months you will pay the installments: '))

installment = loan/months

if installment > salary*0.3:
    print(r'Loan denied. The installment is higher than 30% of your salary')
else:
    print(f'The loan will be done. You will pay {installment} a month')
