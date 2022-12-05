# defining a function
def primeNum(num):
    later_array = []
    
    for  k in range (2, num):
        if num % k == 0:
            later_array.append(k)
    if len (later_array) == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not prime")
        print(f"prime numners before {num} are in this list: {later_array}")
        
    
number = int(input("Enter a number:"))

# calling the function

primeNum(number)

    