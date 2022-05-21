from time import sleep


def highest(*num):

    for i in range(0,len(num)):
        if i == 0:
            high = num[i]
        else:
            if num[i] > high:
                high = num[i]

    print("-="*10)
    print(num)
    print("-="*10)
    sleep(1.3)
    print(f"Highest value: {high}")
    sleep(1.3)


highest(1,2,3,4)
highest(2,0)
