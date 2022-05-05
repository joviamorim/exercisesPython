expression = input("Insert a expression: ")
parentheses = 0

for i in expression:
    if i == ')':
        parentheses-=1
        if parentheses < 0:
            print("Not valid expression.")
            exit()
    elif i == '(':
        parentheses+=1
    
if parentheses != 0:
    print("Not valid expression.")
else:
    print("Valid expression.")
