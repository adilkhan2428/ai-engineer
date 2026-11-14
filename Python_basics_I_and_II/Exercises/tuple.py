# Tuple: Just like list: An ordered, Unchangable collection that  allow duplicate, written with parenthesis --> ()
# It is (IMMUTABLE): It is used when we want the data should not be changed. 

# PART # 1: Creating 
point = (24.56, 45.01, 45.01)
single = (5,)          # the comma makes it a tuple
not_tuple = (5)        # this is just the integer 5
empty = ()

print(point)
print()
print(single)
print()
print(not_tuple)
print()
print(empty)

print(type(point))
print(type(single))
print(type(not_tuple))

# PART # 2: Changing is not allowed:
#point[0] = 30    # this throw an error: TypeError: 'tuple' object doesn't support type assignment

#point.append(1)    # AttributeError: 'tuple' ojbect has no attribute 'append'

# attribute --> a property assign to an object.
# NOTE:  first error is about changing an item. Second as about method that doesn't exist on tuples, Knowing which error is which tells you what went wrong.

# The only methods are --> count() and index()

print(point.count(45.01))
print(point.index(45.01))

# Unpacking: the reason tuples are everywhere

# lat, lon = point  # latitute = 24.86, lonitude = 45.01

# A caution: a tuple is only immutable at its own level. 
a = ([1, 2, 3, 4], 5, 8, 8) 
print(a[0].reverse()) #  <--  Lets we do a[0].reverse()
print(len(a))
print(a[0])   # it change because the inner list is still mutable.


