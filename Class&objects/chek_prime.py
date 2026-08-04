#cheak prime number using class and object 
class PrimeChecker:
    
    def __init__(self):
         PrimeChecker.n= int(input("Enter a number: "))
    
    def is_prime(self):
        if PrimeChecker.n <= 1:
            return False
        for i in range(2, int(self.n ** 0.5) + 1):
            if self.n % i == 0:
                return False
        return True

a= PrimeChecker()
if a.is_prime():
    print(f"{a.n} is a prime number.")
else:
    print(f"{a.n} is not a prime number.")