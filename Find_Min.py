#Write a program which finds the smallest element in the array.
my_list = [1,2,3,4,5, 25]

def my_min(my_list):
    for a in range(len(my_list)-1,-1,-1):
        smallest = my_list[0]
        for a in my_list:
            if a < smallest:
                smallest = a
    return(smallest)

m = my_min(my_list)
print(f"{m} is the smallest number")