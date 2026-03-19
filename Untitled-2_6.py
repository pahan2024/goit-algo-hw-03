pool = 1000
quantity = int(input("Enter the number of mailings: "))

try:
    chunk = round(pool/quantity)
    print(f"{chunk}")

except ZeroDivisionError:

    print('Divide by zero completed!')