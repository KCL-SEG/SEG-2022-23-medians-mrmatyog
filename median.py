"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
sorted_numbers = sorted(numbers)
middle_index = len(sorted_numbers) // 2
if len(sorted_numbers) % 2 == 0:
    median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
else:
    median = sorted_numbers[middle_index]
print(float(median))
