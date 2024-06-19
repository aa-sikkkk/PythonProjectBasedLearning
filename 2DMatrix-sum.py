def sum_matrices(matrix1, matrix2):
    # Get the number of rows and columns in the matrices
    rows = len(matrix1)
    cols = len(matrix1[0])  # Assuming all rows have the same number of columns as the first row
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Iterate through each element and calculate the sum
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Calculate the sum of the two matrices
result = sum_matrices(matrix1, matrix2)

# Print the result
for row in result:
    print(row)
