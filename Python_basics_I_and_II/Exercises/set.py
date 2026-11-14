# Set: An Unordered collection of unique items. written with curly baraces: {3, 5, 6, 9}
# Why it exist: When the question is "which unique things do i have?", a set answers it directly. it also test membership very quickly
# As a list (slow for large datasets)
fraud_list = [1928, 3847, 5920, ...] # 500,000 items
is_fraudulent = 5920 in fraud_list # Python checks index 0, then 1, then 2...

# As a set (instant, regardless of size)
fraud_set = {1928, 3847, 5920, ...} # 500,000 items
is_fraudulent = 5920 in fraud_set # Python jumps straight to it instantly --> this is why we say it (test membership very quickly)

# Part # 1: Creating 
ids = {3, 4, 5, 9}
ids = set([2, 3, 9, 3, 1, 3, 2]) #  {9, 2, 3, 1}, duplicate removed
empty = set()         # not {}, this is not an empty dictinary, 
# Because dictionary come fist in python's history, Python reserved {} to mean an empty dictionary.

my_data = {} # <class 'dict'> --> Python creates a dictionary not a set.
print()

print(ids)
print(type(empty))

# PART # 2: Changing 
ids.add(13)    # adds one item; adding an existing item does nothing 
ids.remove(3)  # KeyError if absent
ids.discard(5) # silently deos nothing if absent
print(ids.pop())     # removes and returns an arbitrary item 


# PART # Set operations 
a = {1, 2, 3} 
b = {2, 3, 4}

print(a | b)   # union: {1, 2, 3, 4} --> customers who bought product A and who bought product B. we can write like this aswell: a.union(b)
print(a & b)   # intersection: {2, 3} --> customers who bought both.
# we can write like this aswell: a.intersection(b)
print(a - b) # defference: {1, 2, 3} --> only those customers who bought product A. not including those who bought product B. 
# we can also write like this: a.defference(b)



# Common Mistakes 
# {} creates a dictionary. Use set() for an empty set.
# Using set when order matters. Converting a list to a set and back can silently reorder your data.

# hash value:  a unique fingerprint calculated from an item's data) to store and look up items instantly.
unhashable_elements = """A set stores each item by a fingerprint, called a hash, so it can find items quickly. Only things that can’t change have a fixed fingerprint. A list can change, so it has none.

Analogy: a set is a guest list at a door. Each guest needs a fixed name tag. A list changes its name tag every time you edit it, so the door can’t check it."""

names = {'shahan', 'jameel', 'behram', 'waseem'}
