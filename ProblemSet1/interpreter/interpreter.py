expression = input("Expression: ")

x, y, z = expression.split(" ")

if z == '0':
    print("You can NOT divide by 0")
else:
    match y:
        case '+':
            result = float(int(x) + int(z))
        case '-':
            result = float(int(x) - int(z))
        case '*':
            result = float(int(x) * int(z))
        case '/':
            result = float(int(x) / int(z))
        case _:
            print("Wrong operator")

    print(result)