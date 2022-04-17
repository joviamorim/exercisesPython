# m = the value of a multiple of a number (in this case 3),
# s = sum of multiples
s = 0
for m in range(0, 20, 3):
    if m%3 == 0:
        s = s+m

print(s)
