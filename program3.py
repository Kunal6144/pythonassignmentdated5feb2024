# Initialize variables for smallest and largest numbers
smallest = None
largest = None

# Get input from the user until an empty string is entered
while True:
    user_input = input("Enter number (or press Enter to quit): ")

    # Check if the user entered an empty string to quit
    if user_input == "":
        break

    # Convert the user input to a float
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Update the smallest and largest numbers
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

# Print the smallest and largest numbers
if smallest is not None and largest is not None:
    print(f"The smallest number entered is: {smallest}")
    print(f"The largest number entered is: {largest}")
else:
    print("No valid numbers entered.")
