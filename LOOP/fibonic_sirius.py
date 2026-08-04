# Fibonacci sequence
i = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(i):
    print(a, end=' ')
    a, b = b, a + b
    