names_output = open('names.txt', 'w')

name = input("Please enter your name")
names_output.write(name)
names_output.close()

names_input = open('names.txt', 'r')
name = names_input.read().strip()
names_input.close()
print("Your name is:", name)

numbers_input = open('numbers.txt', 'r')
number1 = int(numbers_input.readline())
number2 = int(numbers_input.readline())
numbers_input.close()
print(number1 + number2)

numbers_input = open('numbers.txt', 'r')
Total = 0
for line in numbers_input:
    Total += int(line)
numbers_input.close()
print(Total)