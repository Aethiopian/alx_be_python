# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add: "))  # Prompt user for number of days
        future_date = datetime.now() + timedelta(days=days_to_add)  # Calculate future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"Future date after {days_to_add} days: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer.")

# Main function to run the script
def main():
    display_current_datetime()  # Call function to display the current date and time
    calculate_future_date()  # Call function to calculate the future date

if __name__ == "__main__":
    main()
