num = int(input('Enter a number: '))

i = 0
fn1 = 0
fn2 = 1
fn = fn1

print(fn1)
print(fn2)

while i < num-2:
    fn = fn2 + fn1
    print(fn)
    fn1 = fn2
    fn2 = fn
    i += 1
