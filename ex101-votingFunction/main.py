from datetime import datetime

def verify(age):
    if (age>16 and age<18) or age>65:
        situation = "Optional"
    elif age<16:
        situation = "Prohibited"
    else:
        situation = "Mandatory"

    return situation


birth = int(input("Insert your birth year: "))
age = datetime.today().year - birth
print(f"Age: {age}. The voting is {verify(age)}")
