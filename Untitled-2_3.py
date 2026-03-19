num = int(input("Enter a number: "))

if num>0:
    if num %2 == 0:
        result = "Positive even number"
        
    else:
        result = "Positive odd number"
elif num <0:
    result = "Negative number"
else:
    result = "It is zero"
print(result)
