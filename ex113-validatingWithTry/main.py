def readInt(msg=""):
    while True:
        try:
            value = 0
            n = str(input(msg))
            value = int(n)
        except Exception as error:
            print(f"Error: {error}")
            continue
        else:
            return value


def readFloat(msg=""):
    while True:
        try:
            n = float(input(msg))    
        except Exception as error:
            print(f"Error: {error}")
            continue
        else:
            return n


intNum = readInt("Type a int number: ")
floatNum = readFloat("Type a float number: ")
print(intNum)
print(floatNum)
