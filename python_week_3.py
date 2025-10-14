def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price: The original price of the item
        discount_percent: The discount percentage to apply
    
    Returns:
        The final price after discount (if applicable), or original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
if __name__ == "__main__":
    try:
        # Get user input
        price = float(input("Enter the original price of the item (ZAR): R"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Display results
        if discount_percent >= 20:
            print(f"\nDiscount applied: {discount_percent}%")
            print(f"Original price: R{price:.2f}")
            print(f"Final price: R{final_price:.2f}")
            print(f"You saved: R{price - final_price:.2f}")
        else:
            print(f"\nDiscount of {discount_percent}% is below the 20% minimum.")
            print(f"Original price: R{price:.2f}")
            print(f"Final price: R{final_price:.2f} (no discount applied)")
    
    except ValueError:
        print("Error: Please enter valid numeric values for price and discount percentage.")
