values =[]

for i in range(0,5):
    values.append(int(input("Insert a number: ")))
    
    if i == 0:
        high = values[i]
        low = values[i]
    elif values[i] > high:
        high = values[i]
    elif values[i] < low:
        low = values[i]

posHigh = values.index(high)
posLow = values.index(low)

print(f"Highest number: {high}. Position: {posHigh}")
print(f"Lowest number: {low}. Position: {posLow}")
