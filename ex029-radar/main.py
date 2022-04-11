speed = int(input('Insert the car speed: '))

limitSpeed = 80.00

if speed>limitSpeed:
    speedDiff = speed - limitSpeed
    fine = speedDiff*7.00
    print(f'{speed}. Maximum speed exceeded. Fine: {fine}')

print(f'{speed}. No penalities.')
