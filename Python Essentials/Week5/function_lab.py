# Function_lab.py

# Function: Calculate total price
# input: Price, Quantity
# Output: Total Price
def total_cost(price, quantity):
    return price * quantity


# Function: Apply a discount percentage
# Input: Amount, Discount Percentage
# Output: Discounted Amount
def apply_discount(Amount, Discount_Percentage):
    discount_amount = Amount * (Discount_Percentage / 100)
    return Amount - discount_amount

# function: Add Sales Tax
# Input: Amount, Tax Percentage
# Output: Amount with Tax
def add_tax(amount, tax_rate):
    return amount + (amount * (tax_rate / 100))

def main():
    subtotal = total_cost(40, 5)
    discounted = apply_discount(subtotal, 30)
    final_price = add_tax(discounted, 7)

    print("Subtotal:", subtotal)
    print("After discount:", discounted)
    print("Final price with tax:", final_price)


if __name__ == "__main__":
    main()