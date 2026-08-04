"""Sets In Python
Set is a collection of non-repetitive elements.
s = set() # no repetition allowed!
 s.add(1)
 s.add(2) # or set ={1,2}
If you are a programming beginner without much knowledge of mathematical operations on sets, you can
simply look at sets in python as data types containing unique values.
Properties Of Sets
Sets are unordered => Element’s order doesn’t matter
Sets are unindexed => Cannot access elements by index
There is no way to change items in sets.
Sets cannot contain duplicate values.
Operations On Sets
Consider the following set:
s = {1,8,2,3}
len(s): Returns 4, the length of the set
s.remove(8): Updates the set s and removes 8 from s.
s.pop(): Removes an arbitrary element from the set and return the element removed.
s.clear(): empties the set s.
s.union({8,11}): Returns a new set with all items from both sets.
s.intersection({8,11}): Returns a set which contains only item in both sets {8"""