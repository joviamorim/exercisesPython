def sysDocs(name):
    """
    Shows documentations for functions and libraries
    name -> function or library name
    """
    help(name)


while True:
    name = str(input("Function or Lib > "))

    if name.upper() == "END":
        break
    else:
        sysDocs(name)
    