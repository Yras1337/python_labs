def calc(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mult":
        return num1 * num2
    elif operation == "div":
        return num1 / num2 if num2 != 0 else "Cannot divided by zero"
    else:
        return "Incorrect operator"


def get_even_number_list(lst):
    return list(item for item in lst if item % 2 == 0)


print("Hello world")

# check calc func
while True:
    try:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        break
    except ValueError:
        print("Incorrect input! Try again: ")

while True:
    operation = input("Enter operation(add, sub, mult, div): ")
    result = calc(num1, num2, operation)
    if result != "Incorrect operator":
        print("Result:", result)
        break
    else:
        print(result)

# check even list function
while True:
    try:
        length = int(input("Input length of list: "))
        break
    except ValueError:
        print("Incorrect input! Try again: ")

lst = []
for i in range(length):
    while True:
        try:
            item = int(input("Input item " + str(i) + " of list: "))
            lst.append(item)
            break
        except ValueError:
            print("Incorrect input! Try again: ")

print(get_even_number_list(lst))