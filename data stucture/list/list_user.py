# list input from the user
a = []
n = int(input("Enter the number of elements in the list: "))
print("Enter", n, "numbers:")
for i in range(n):
    num = int(input())
    a.append(num)
print(a)