"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

is_valid_input = False
while not is_valid_input:
    try:
        score = float(input("Enter score: "))
        if score < 0 or score > 100:
            print("The scores must be in between 0 and 100")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid Choice (must be an integer)")

if score > 89:
    print("Excellent")
elif score > 49:
    print("Passable")
elif score < 50:
    print("Bad")