words = ("banana", "phone", "church", "table")

for w in words:
    print(w.upper(), end=":")
    '''for i in range(0,len(w)):
        if w[i]=='a' or w[i]=='e' or w[i]=='i' or w[i]=='o' or w[i]=='u':
            print(f" {w[i]}", end="")'''

    for i in w:
        if i in "aeiou":
            print(f" {i}", end="")

    print("")
