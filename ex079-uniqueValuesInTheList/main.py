values = []

while True:
    v = int(input("Insert the value: "))
    
    if v in values:
        print("Already existing value.")
    else:
        values.append(v)
    
    add = input("Add other value? (y=yes, n=no)\n")

    if add == 'n':
        break

values.sort()

print(f"All unique values sorted: {values}")
