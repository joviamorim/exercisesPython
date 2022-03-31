num = int(input('Type a number (until 9999): '))

# separating the digits of a number
thousand = num//1000
num = num%1000

hundred = num//100
num = num%100

ten = num//10
num = num%10

one = num

# other way
# thousand = num // 1000 % 10
# hundred = num // 100 % 10
# ten = num // 10 % 10
# one = num // 1 % 10

print(f'Thousands: {thousand}')
print(f'Hundreds: {hundred}')
print(f'Tens: {ten}')
print(f'Unities: {one}')
