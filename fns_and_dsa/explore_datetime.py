from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date
    current_date = datetime.now()

    # Print in "YYYY-MM-DD HH:MM:SS" format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Save the future date
    future_date = datetime.now() + timedelta(days=days)

    # Print in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Ask for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
