# Take input from the user and find out if that number is prime or not.

num = int(input("Type a number to determine if your number is a Prime number: "))

if num > 1:
        for i in range(2, num):
            if num % i == 0:
             print("NOT a prime number!")
             break
        else:
            print("Prime Number!")

else:
    print("NOT a Prime Number!")
