def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return factorial(n)// (factorial(k)* factorial(n-k))

print (number_of_groups(50,7))
    
    
    