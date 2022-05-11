from datetime import datetime

worker = dict()

worker['name'] = str(input("Insert your name: "))

birthYear = int(input("Insert your year of birth: "))
age = datetime.today().year - birthYear
worker['age'] = age

worker['workCard'] = int(input("Insert your work card (0 if you don't have): "))

if worker['workCard'] != 0:
    hiringYear = int(input("Insert the hiring year: "))
    retirementAge = (datetime.today().year - hiringYear) + 35 + worker['age']
    worker['retirementAge'] = retirementAge

    worker['salary'] = float(input("Insert the salary: "))

for k,v in worker.items():
    print(f"{k}: {v}")
