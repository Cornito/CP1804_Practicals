"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


#sales = float(input("Enters amount of sales: $"))

#while sales < 0:
#    sales = float(input("Not an available choice, please enter an amount of sales: $"))

# is_valid_input = False
# while not is_valid_input:
#     try:
#         sales = float(input("Enters amount of sales: $"))
#         if sales < 0:
#             print("Sales must be greater then 0")
#             exit("You have entered a negative number now quitting program")
#         else:
#             is_valid_input = True
#     except ValueError:
#         print("Invalid choice (not an integer)")
# if sales >= 1000:
#     bonus = sales / 100 * 15
#     total = bonus + sales
#     print("Your bonus for ${} worth of sales is: ${}, Total earned = ${}".format(sales, bonus, total))
# elif sales < 1000:
#     bonus = sales / 100 * 10
#     total = bonus + sales
#     print("Your bonus for ${} worth of sales is: ${}, Total earned = ${}".format(sales, bonus, total))

sales =  float(input("enter sales"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales / 100 * 15
        total = bonus + sales
        print("Your bonus for ${} worth of sales is: ${}, Total earned = ${}".format(sales, bonus, total))
    else:
        bonus = sales / 100 * 10
        total = bonus + sales
        print("Your bonus for ${} worth of sales is: ${}, Total earned = ${}".format(sales, bonus, total))
    sales = float(input("enter sales"))
print("You have entered negative number, now exiting")