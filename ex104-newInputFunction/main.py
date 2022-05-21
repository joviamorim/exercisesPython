def readInt(msg=""):
    value = 0
    n = str(input(msg))
    if n.isnumeric():
        value = int(n)
        return value
    else:
       return "Enter numbers only"

    
num = readInt()
print(num)
