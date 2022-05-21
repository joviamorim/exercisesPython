import menu

def arqExist(name):
    try:
        arq = open(name, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createArq(name):
    try:
        arq = open(name, 'wt+')
    except Exception as error:
        print(f"Error: {error}")
    else:
        print(f"File {name} created.")

def readArq(name):
    try:
        arq = open(name, 'rt')
    except Exception as error:
        print(f"Error: {error}")
    else:
        txt = arq.read()
        arq.close()
        menu.display(txt)


def addArq(arq="", name="", age=0):
    try:
        a = open(arq, 'at')
    except:
        print("Error.")
    else:
        try:
            a.write(f"{name:<22}{age}\n")
        except:
            print("Error on write.")
        else:
            print("User added.")
        finally:
            a.close()

