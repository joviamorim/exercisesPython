# item --> price --> item --> price
priceList = ("Apple", 1.50, "Coconut", 4.70, "Banana", 5.40, "Tomato", 2.30)
i = 0

while i<len(priceList):
    if i%2==0:
        print(f"{priceList[i]:.<10}", end="")
    else:
        print(f"{priceList[i]}")
    i+=1
