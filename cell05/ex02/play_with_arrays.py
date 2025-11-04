import sys

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

processed_array = [
    element + 2 for element in original_array if element > 5
]

print(original_array)

print(processed_array)