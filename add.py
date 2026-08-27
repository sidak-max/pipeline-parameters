import sys

# Define two numbers by pulling from command-line parameters
# sys.argv[0] is the script name, sys.argv[1] is NUM1, sys.argv[2] is NUM2
try:
    number_one = int(sys.argv[1])
    number_two = int(sys.argv[2])
except IndexError:
    # Fallback default values if no arguments are passed
    number_one = 5
    number_two = 10

# Calculate the sum
result = number_one + number_two

# Display the result
print(f"The sum of {number_one} and {number_two} is {result}")
