import numpy as np
marks = np.array([[44, 56, 78, 90, 34, 65],
                  [78, 90, 87, 52, 73, 32]])
marks2 = np.array([[97, 56, 78, 56, 34, 65],
                  [34, 90, 87, 52, 73, 87]])
# Saving and loading arrays
#np.savez_compressed("multipleMarks_compressed", marks, marks2)
#array = np.load("D:\\Numpy-Saving-Loading.npy")
arr = np.load("multipleMarks_compressed.npz")
print(arr)
new_marks = arr["arr_0"]
new_marks2 = arr["arr_1"]
print(new_marks)
print(new_marks2)
print("Successful!")