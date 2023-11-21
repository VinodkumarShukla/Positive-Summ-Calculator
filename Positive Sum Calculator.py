def sum_positive_numbers(numbers):
    # Filter positive numbers and calculate their sum
    positive_numbers = [num for num in numbers if num > 0]
    sum_positives = sum(positive_numbers)
    return sum_positives

# Example usage:
numbers_str = input("Enter a list of integers separated by spaces: ")

# Convert the input string to a list of integers
numbers = [int(num) for num in numbers_str.split()]

# Calculate the sum of positive numbers
result = sum_positive_numbers(numbers)

# Display the result
print(f"The sum of positive numbers is: {result}")
