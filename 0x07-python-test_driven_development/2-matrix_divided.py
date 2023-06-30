#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all the elements of a matrix by a divider

    Parameters:
    matrix: a list of lists of integers and floats
    div: a number, whether integer or float

    Return:
    A new matrix with the divded elements

    Raises:
    TypeError

    """
    new_matrix = []
    check_int = all(isinstance(a, list) and all(
        isinstance(num, int) for num in a) for a in matrix)
    check_float = all(isinstance(b, list) and all(
        isinstance(num, int) for num in b) for b in matrix)

    if not check_int:
        raise TypeError("matrix must be a matrix 
        (list of lists) of integers/floats")
    elif not check_float:
        raise TypeError("matrix must be a matrix 
        (list of lists) of integers/floats")
    elif div == 0:
        raise ZeroDivisionError("divdision by zero")
    elif not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")
    for inner in matrix:
        for num in inner:
            new = num / div

