# (**kwargs)
# Variable keyword argument: This allow us to pass data as (key-value) pair, 
# this is very useful when the order of the data might changes, as python stores
# in dictionary inside the function.

# def create_order(**order):
#     print(order)
#     print(type(order))

# create_order(item='hoodie', qty = 2, price=1800)

# Task: 
def make_student(**info):
    info.setdefault('status', 'active') # this set the default as active but if status already present so, it don't override it. 
    return info

print(make_student(name="Zaman", class_no=12))
# {'name': 'Zaman', 'class_no': 12, 'status': 'active'}

print(make_student(name="Ali", status="inactive"))
# {'name': 'Ali', 'status': 'inactive'} # keep inactive, don't overwrite