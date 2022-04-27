nums = (int(input("Value: ")), int(input("Value: ")), int(input("Value: ")), int(input("Value: ")))

for i in nums:
    print(f"{i} ", end="")

num9 = nums.count(9) # counting the nines
print(f"\nNumber of nines: {num9}")

if 3 in nums:
    index3 = nums.index(3) # index of first 3
    print(f"Index of first number 3: {index3}")

print("Pair numbers: ", end="")
for i in nums:
    if i%2==0:
        print(f"{i} ",end="")
