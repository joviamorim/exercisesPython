def discount(c, f=True):
    disc = c*0.9
    if f:
        disc = currency(disc)

    return disc

def half(c, f=True):
    h = c/2
    if f:
        h = currency(h)

    return h

def twice(c, f=True):
    tw = c*2
    if f:
        tw = currency(tw)

    return tw

def currency(c):
    strC = str(c).replace('.',',')
    fCurrency = "R$"+strC

    return fCurrency

def abstract(c, f=True):
    print(f"Value with discount: {discount(c,f)}")
    print(f"Half value: {half(c,f)}")
    print(f"Twice the value: {twice(c,f)}")
