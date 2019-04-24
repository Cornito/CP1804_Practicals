
Items = list()
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Number of items must be greater than zero")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    list.append(Items, price_of_item)

TotalPrice = sum(Items)
if TotalPrice > 100:
    discount = TotalPrice * .1
    TotalPrice -= discount

print("Total price for {} items is ${}".format(number_of_items, TotalPrice))



