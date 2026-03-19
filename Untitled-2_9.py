price=100
discount = 0.1
def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price *= (1 - discount)

    apply_discount()
    return price
print(price)

def discount_price(price, discount):
    # Nested function to apply discount
    def apply_discount():
        nonlocal price  # Use nonlocal to modify the outer 'price' variable
        price = price * (1 - discount)  # Apply discount formula

    apply_discount()  # Call the nested function to update price
    return price  # Return the discounted price
print(price)