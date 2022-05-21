def counter(s,e,st):    # s-> start, e -> end, st -> step
    for i in range(s,e,st):
        print(i)


start = int(input("Enter the initial number: "))
end = int(input("Enter the final number: "))
step = int(input("Enter the step: "))

counter(start, end, step)
