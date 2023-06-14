#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''This function computes the square value of all integers of a matrix'''
    # Creating a new matrix to return
    the_matrix = []
    # Looping through the matrix
    for i in matrix:
        the_matrix_row = []
        for j in i:
            result = j * j
            # appending the result in the row
            the_matrix_row.append(result)
        # appending the result to the main matrix
        the_matrix.append(the_matrix_row)
    return (the_matrix)
