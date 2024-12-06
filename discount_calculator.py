# Define the function
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is less than 20%, no discount is applied.
    
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.
        
    Returns:
        float: The final price after applying the discount, or the original price.
    """
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount
    return price

# Main script to prompt user and display results
if __name__ == "__main__":
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Call the function
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display the result
        if discount_percentage >= 20:
            print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${original_price:.2f}")
    except ValueError:
        print("Please enter valid numerical values for price and discount percentage.")
