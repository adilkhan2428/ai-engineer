# List: An ordered, changable collection that allows duplicate, written with square brackets [120, 40, 56, 34]
# Why it Exist: Most order data is sequence that grows or gets edited. a cart's items, dail order totals, a queue of support tickets.
# PART # 1: Creating and Reading: 
totals = [120, 45, 300, 80, 60, 90, 65]
print(totals[0])
print(totals[-1]) # 80, last element
print(len(totals)) # 4 --> number of items
print(300 in totals)

# PART # 2: Changing a list
totals.append(220)
totals.insert(3, 301)
totals.remove(90) # remove the FIRST matching value: ValueError if absent
last = totals.pop()    # remove and return the item
first = totals.pop(1)  # remove and return the item at postion 1
totals[0] = 450        # replaces the item at position index
totals.extend([47, 89, 90]) # adds several items to the end of list

print(totals)
print(last)
print(first)

# PART # 3: Searching and ordering
print(totals.count(90))
print(totals.index(80)) # postion of first 300; ValueError if absent
print(totals.sort())
new = sorted(totals) # return a NEW sorted list, original unchanged.
print(totals.reverse())
print()
print(new)

# PART # 4: Combining
x = [1, 2] + [3]
z = [5] * 5
print(x)
print()
print(z)

# PART # 5: The most important trap: list ar shared by reference
a = [1, 2, 3]
b = a          # b os NOT a copy; both names point to the same list
print(b.append(4)) 
print(a)       # [1, 2, 3, 4]

c = a.copy()   # a real copy; changes to c won't affect a

# PART # 6: Nested List

nested = [3, 4, 5, 8,['adil', 'abas', 'atif']]

print(nested[4][2])

# PART # 7: Multiple types of data can be stored.

mixed = [1, 2, 3, 'adil', 'atif', 'jameel', 45.66, 90.99, True, False]

# PART #  we can also write the (tuple) and (set) in a list

hybrid_list = [1, 2, 3, 4, 5, ('a', 'b', 'c'), {'A', 'B', 'C'}]
print(hybrid_list)



