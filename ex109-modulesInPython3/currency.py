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
    fCurrency = "R$"+str(c)

    return fCurrency

        
