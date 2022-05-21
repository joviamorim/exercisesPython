def factorial(n):
    """
    n -> factorial number
    this function returns the result of the factorial
    """
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact


fact = factorial(4)
print(fact)
help(factorial)
