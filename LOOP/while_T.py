
try:
    a=int(input("Enter a number: "))

except ValueError:
    print("Invalid input. Please enter a valid integer.") 
    while True:
        try:
            a=int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.") 