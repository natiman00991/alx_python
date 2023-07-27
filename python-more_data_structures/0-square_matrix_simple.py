def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    new_matrix = []

    # Loop through each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values for this row
        squared_row = []

        # Loop through each element in the row and square it
        for num in row:
            squared_row.append(num**2)

        # Add the squared row to the new matrix
        new_matrix.append(squared_row)

    return new_matrix


# # Test the function with the given matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
# print(matrix)
