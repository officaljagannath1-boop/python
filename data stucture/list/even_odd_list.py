a=[2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("The count of even numbers is:", even_count)
print("The count of odd numbers is:", odd_count)