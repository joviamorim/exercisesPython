# get the wall dimension
width = float(input('Wall width in meters: '))
height = float(input('Wall height in meters: '))

# get the ink yield per m²
inkYield = float(input('The ink yield in liters per m²: '))

# calculation (height*width)/inkYield
totalInk = (height*width)/inkYield

print(f'The total ink needed to fill the wall is: {totalInk} liters')
