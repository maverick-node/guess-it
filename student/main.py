import sys
import math
import statistics

def read_data():
    data = []
    while True:
        try:
            # Read a line of input
            input_data = input()
            # If input is empty, break the loop
            if not input_data:
                break
            num = float(input_data)
            data.append(num)
        except ValueError:
            # Handle invalid input
            print("Invalid input!!!")
            break
    return data

def average(data):
    return statistics.mean(data)

def deviation(data):
    if len(data) < 2:
        return 0
    return statistics.stdev(data)

def main():
    data = read_data()

    if not data:
        print("Error: No valid data found.")
        sys.exit(1)

    # Initialize the max value to the first element of data
    max_value = 0
    numbers = []

    for num in data:
        # Only consider numbers within 500 of the current max_value
        if abs(num - max_value) < 500:
            max_value = max(max_value, num)
            numbers.append(num)

        # Calculate average and deviation of the current list of numbers
        avg = average(numbers)
        dev = deviation(numbers)

        # Output the difference and sum of avg and dev
        print(f"{abs(avg - dev)} {avg + dev}")

if __name__ == "__main__":
    main()
