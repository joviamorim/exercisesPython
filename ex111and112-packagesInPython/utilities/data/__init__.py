from utilities import currency

def verify(c):
    strC = str(c).replace(',','.')

    if strC.isalpha():
        print("Invalid value") 
    else:
        floatC = float(strC)
        currency.abstract(floatC)
                
