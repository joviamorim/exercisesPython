h = 0 # highest number
l = 0 # lowest number

for i in range(0,5):
    num = int(input(f'Enter the value number {i}: '))

    if num > h:
        h = num
    else:
        if num < l:
            l = num
    
print(f'Highest number: {h}')
print(f'Lowest number: {l}')
