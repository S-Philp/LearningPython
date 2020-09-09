num = input("Type a number: ")
user_num = int(num)

if user_num%3==0:
    print("Fizz")
if user_num%5==0:
    print("Buzz")

elif user_num%3==0 and user_num%5==0:
    print("FizzBuzz")
