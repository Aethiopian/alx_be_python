# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Check if the input is a positive integer
if size > 0:
    # Draw the pattern
    row = 0
    while row < size:  # Iterate through each row
        for col in range(size):  # Print asterisks in each column
            print("*", end="")  # Print without newline
        print()  # Move to the next row
        row += 1  # Increment the row counter
else:
    print("Please enter a positive integer.")
