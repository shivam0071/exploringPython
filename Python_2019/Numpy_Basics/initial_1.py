# 22/July/2019
# 6:34 PM

# Numpy Arrays

import numpy as np

ls = [1,2,3,4]
arr = np.array(ls)
print("Vector")
print(arr)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(matrix)
print("\nMATRIX")
print(mat)


print("\nVector from A RANGE")
reshape_this = np.arange(1,25,2)
print(np.arange(1,25,2))


print("\n Zero Vector")
print(np.zeros(3))

print("\n Zero Matrix")
print(np.zeros((3,4))) # 3 rows 4 columns

print("\n Ones Vector/Matrix")
print(np.ones((2,3)))


print("\n Linspace or a vector made from 2 numbers")
print(np.linspace(0,10,5))
# 5d vector from number between 0 to 10

# Identity Matrix
print("\nIdentity Matrix")
print(np.eye(3))

# Random no Matrix and Vector

print("\n Random Matrix from 0 to 1")
print(np.random.rand(4))
print(np.random.rand(4,3))
print(np.random.randn(3,4))  # not 0 to 1

print("\n Random Matrix bet 2 int")
r_arr = np.random.randint(1,100,10)
print(np.random.randint(1,100,10)) # 10d vector from 2 numbers


# Reshape arrays
print("\nReshape This")
print(reshape_this)
print(reshape_this.reshape(3,4))


print("Basic Operations")
print(r_arr)
print(f"Max {max(r_arr)}")
print(f"Min {min(r_arr)}")
print(f"Position for Max {r_arr.argmax()}")
print(f"Position for Max {r_arr.argmin()}")
print(f"Type of Matrix {r_arr.shape}")