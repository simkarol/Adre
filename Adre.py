import numpy as np

# I. Matrix Creation
print("Initials: SMA -> [19, 13, 1]")
print("Second letters: IAD -> [9, 1, 4]")

# Student: Sim Karol Maniego Adre
# Student ID: 2023-4-0090

# Values based on initials and second letters
first_matrix = np.array([[19, 13, 1], [9, 1, 4]])
second_matrix = np.array([[2, 0, 2], [0, 9, 0]])

# Function to print matrix with commas
def print_matrix(matrix):
    formatted = "[\n"
    for row in matrix:
        formatted += " [" + ", ".join(map(str, row)) + "],\n"
    formatted = formatted.rstrip(",\n") + "\n]"
    print(formatted)

# Showing the two matrices
print("\nI. Displaying the two matrices:")
print("First Matrix:")
print_matrix(first_matrix)
print("\nSecond Matrix:")
print_matrix(second_matrix)

# II. Adding Matrices
print("\nII. Adding the Matrices")

sum_matrix = first_matrix + second_matrix

print("\nResulting Matrix after Addition (First + Second):")
print_matrix(sum_matrix)

# III. Multiplying by a Scalar
print("\nIII. Multiplying First Matrix by a Scalar")

scalar_multiplied_matrix = first_matrix * 2

print("\nScalar Multiplied Matrix (First Matrix × 2):")
print_matrix(scalar_multiplied_matrix)

# IV. Transposing a Matrix
print("\nIV. Transposing Second Matrix")

transposed_matrix = second_matrix.transpose()

print("\nTransposed Matrix (Second Matrix Transposed):")
print_matrix(transposed_matrix)

# V. Matrix Multiplication
print("\nV. Performing Matrix Multiplication")

product_matrix = np.dot(sum_matrix, transposed_matrix)

print("\nMatrix Product (Sum Matrix × Transposed Matrix):")
print_matrix(product_matrix)

# VI. Summing All Elements
print("\nVI. Summing Elements of the Sum Matrix")

elements_total = np.sum(sum_matrix)

print("\nTotal of All Elements in Sum Matrix:")
print(elements_total)

# VII. Generating a Zero Matrix
print("\nVII. Creating a Zero-Filled Matrix")

zero_matrix = np.zeros((2, 3), dtype=int)

print("\nZero-Filled Matrix (2x3):")
print_matrix(zero_matrix)
