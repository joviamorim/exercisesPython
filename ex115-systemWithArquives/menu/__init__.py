import archive

arq = 'data.txt'


def line(n = 24):
    return "-"*n

def add():
    print(line())
    name = str(input("Insert the name: "))
    age = int(input("Insert the age: "))
    archive.addArq(arq,name,age)
    print(line())

def display(txt):
    print(line())
    print(txt)
    print(line())

def menu():
    print(line())
    print("Menu".center(24))
    print(line())
    while True:
        try:
            n = int(input("1 - Add a user.\n2 - Display the users.\n3 - Exit.\n"))
        except ValueError:
            print("Insert a valid value.")
        else:
            if n == 1:
                add()
            elif n == 2:
                archive.readArq(arq)
            else:
                exit()

