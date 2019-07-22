import numpy as np

arr = np.arange(0,10)
print(arr)
print(arr[0])
print(arr[:6])
slice = arr[:6]
print(slice)
slice[:] = 100
print(slice)
print(arr)

# use arr.copy to copy the actual array

# 2D Array
arr_2d = np.array([[1,2,3],[44,5,5],[55,332,22]])
print(arr_2d)
print(arr_2d[1][1])
print(arr_2d[1,1])
print(arr_2d[:2,1:]) # first 2 rows and last 2 columns
print(arr_2d[1:,:])


arr = np.arange(1,11)
print(arr)
print(arr > 5)
print(arr[arr > 5]) # only elements greater than 5


arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(arr_2d[1:3,3:5])