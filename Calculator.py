number_1 = int(input("Type a number: "))
opperand = (" +, -, *, / ")
opperand = input("Type an mathematical operation symbol: ")
number_2 = int(input("Type another number: "))

if opperand == '+' :
    answer = number_1 + number_2
    print(answer)
if opperand == '-' :
    answer = number_1 - number_2
    print(answer)
if opperand == '*' :
    answer = number_1 * number_2
    print(answer)
if opperand == '/' :
    answer = number_1 / number_2
    print(answer)
