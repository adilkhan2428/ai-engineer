# Day 1 recap

# 1. Types: every value has a type, and the type decides what operations mean

# python
type("49.99")   # <class 'str'>
type(49.99)     # <class 'float'>
"49.99" * 3     # '49.9949.9949.99'  silent, wrong for money
"49.99" + "10"  # '49.9910'          silent, wrong for money
"49.99" + 10    # TypeError: crashes loudly (the safe failure)
float("49.99") * 3   # 149.97

# Silent wrong results are the real danger, not crashes.

# 2. Conversion and tax

# python
total_with_tax = float("49.99") * 1.15   # 57.4885

# 3. String cleaning (methods return a new string)

# python
raw = [" PK ", "us", " Uk", "PK  ", " ae "]
c0 = raw[0].strip().lower()   # positions start at 0
clean = [c0, c1, c2, c3, c4]  # ['pk','us','uk','pk','ae']

4. // and % (boxes model)

# python
10 // 3   # 3  full boxes
10 % 3    # 1  left over
9 % 3     # 0

# 5. f-strings: :.2f formats the display only

# python
total = 57.4885
label = f"Order {1042} | ali | {total:.2f}"   # 'Order 1042 | ali | 57.49'
print(total)                 # 57.4885, unchanged
total = round(total, 2)      # this actually changes the stored value

# Grades so far: Entry 1/4. Drills: after hint on the list cleaning, cold on the rest. Weak spots: str + int raises TypeError and doesn’t glue, and you skip writing predictions unless prompted.