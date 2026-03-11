# Odd count variable
odd_count = 0

# Input numbers
for i in range(10):
    num = int(input("Enter number: "))

    if num % 2 != 0: # Check if number is odd
        odd_count += 1

# Print odd count
print("Number of odd numbers:", odd_count)