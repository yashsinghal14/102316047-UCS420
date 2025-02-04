import numpy as np

# Q1: 
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# a) 
arr_add = arr + 2
print("After adding 2:", arr_add)

# b) 
arr_mul = arr * 3
print("After multiplying by 3:", arr_mul)

# c) 
arr_div = arr / 2
print("After dividing by 2:", arr_div)

# Q2: 
# a) 
arr2 = np.array([1, 2, 3, 6, 4, 5])
arr_rev = arr2[::-1]
print("Reversed Array:", arr_rev)

# b) 
def most_frequent(arr):
    vals, counts = np.unique(arr, return_counts=True)
    max_count = np.max(counts)
    most_frequent_value = vals[np.argmax(counts)]
    indices = np.where(arr == most_frequent_value)[0]
    return most_frequent_value, indices

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

x_value, x_indices = most_frequent(x)
y_value, y_indices = most_frequent(y)

print(f"Most frequent value in x: {x_value}, Indices: {x_indices}")
print(f"Most frequent value in y: {y_value}, Indices: {y_indices}")

# Q3: 
a_arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Element at (1st row, 2nd column):", a_arr[0, 1])
print("Element at (3rd row, 1st column):", a_arr[2, 0])

# Q4: 
my_array = np.linspace(10, 100, 25)
print("Array:", my_array)
print("Dimensions:", my_array.ndim)
print("Shape:", my_array.shape)
print("Total elements:", my_array.size)
print("Data type:", my_array.dtype)
print("Total bytes consumed:", my_array.nbytes)

# Transpose 
transposed_array = my_array.reshape(25, 1)
print("Transposed Array using reshape():\n", transposed_array)

# Using T attribute 
print("Transpose using T attribute:", my_array.T)

# Q5: 
ucs420_myname = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print("Mean:", np.mean(ucs420_myname))
print("Median:", np.median(ucs420_myname))
print("Max:", np.max(ucs420_myname))
print("Min:", np.min(ucs420_myname))
print("Unique Elements:", np.unique(ucs420_myname))

# Reshape to 4x3
reshaped_ucs420 = ucs420_myname.reshape(4, 3)
print("Reshaped Array (4x3):\n", reshaped_ucs420)

# Resize to 2x3
resized_ucs420 = np.resize(ucs420_myname, (2, 3))
print("Resized Array (2x3):\n", resized_ucs420)
