# Conversion factor from inches to centimeters
INCH_TO_CM = 1.54

# Get initial input from the user
inches = float(input("Enter a length in inches (or a negative value to end): "))

# Use a while loop to convert inches to centimeters until a negative value is entered
while inches >= 0:
    # Perform the conversion and print the result
    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters")

    # Get the next input from the user
    inches = float(input("Enter another length in inches (or a negative value to end): "))

print("Program ended.")
