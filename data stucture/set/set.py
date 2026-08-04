# set in python
s = {1, 2, 3, 4, 5}
print(s)  # Output: {1, 2, 3, 4, 5}
#METHODS
# add() method  
s.add(6)
print(s)  # Output: {1, 2, 3, 4, 5, 6}
# remove() method
s.remove(3)
print(s)  # Output: {1, 2, 4, 5, 6}
# pop() method
removed_element = s.pop()
print(removed_element)  # Output: 1 (or any arbitrary element)
print(s)  # Output: {2, 4, 5, 6}
# clear() method
s.clear()
print(s)  # Output: set()
