import math

ang = float(input('Type the angle you want: '))

# Converting the angle to radian
radian = math.radians(ang)
s = math.sin(radian)
c = math.cos(radian)
t = math.tan(radian)

print(f'Sin: {s:.2f}')
print(f'Cos: {c:.2f}')
print(f'Tg: {t:.2f}')
