# with open("files_save_test/test.txt", 'w', encoding='utf-8') as f:
#     f.write("Hello this is me adil khan!\n"
#     "this was my first time to save the file\n"
#     "we are learning this in python basics II")
    
# print("File Saved successfully!")

# with open("files_save_test/test.txt", 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())

# order_ids = [1001, 1002, 1003, 1004, 1005]

# with open("files_save_test\\orders.txt", 'w', encoding=
# 'utf-8') as f:
#     for id in order_ids:
#         f.write(f"{id}\n")
# with open("files_save_test\\orders.txt", 'a', encoding='utf-8') as f:
#     f.write("Order Processed\n")

my_file = open("files_save_test\\orders.txt", 'r')
order = my_file.read()
print(order)
my_file.close()



