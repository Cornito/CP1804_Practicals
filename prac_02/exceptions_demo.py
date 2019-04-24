"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    denominator = 0
    numerator = int(input("Enter the numerator: "))
    while denominator <= 0:
        denominator = int(input("please enter a denominator GREATER THAN 0: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1: When will a ValueError occur
# A1: When the num or den is a decimal or a letter

# Q2: When will a ZeroDivisionError occur
# A2: If the denominator is a zero

