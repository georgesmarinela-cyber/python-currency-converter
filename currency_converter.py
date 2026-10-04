def convert_eur_to_usd(eur_amount: float) -> float:
    """Convert an amount from EUR to USD (using a fixed conversion rate of 1.1)."""
    rate = 1.1
    return eur_amount * rate

def main():
    print("=== Python Currency Converter ===")
    
    # Get user input from the console
    user_input = input("Enter an amount in EUR to convert: ")
    
    try:
        # Convert user input string into a float
        eur_amount = float(user_input)
        
        # Check if the entered amount is valid
        if eur_amount < 0:
            print("Error: The amount cannot be negative.")
        else:
            usd_result = convert_eur_to_usd(eur_amount)
            print(f"{eur_amount} EUR is equal to {usd_result:.2f} USD.")
            
    except ValueError:
        # Handle cases where user input is not a valid number
        print("Error: Please enter a valid numerical value.")

if __name__ == "__main__":
    main()
