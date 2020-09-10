# Write an app which asks users for the input and then prints the factorial for that number.

n = int(input("Type a number to calculate it's factorial: "))

def factorial(n) :
    if n == 0:
        return 1
    else:    
        return n * factorial (n - 1)
    
print(factorial(n))