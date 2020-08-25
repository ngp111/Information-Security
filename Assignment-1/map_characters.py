import math

def countDigit(n): 
    """ Counts the digits of given number, n """
    if(n==0) : return 1
    return math.floor(math.log(n, 10)+1) 

def generate_codes(matrix) :
    """
        Generate a encoding dictionary mapping each ascii value in matrix to their position in matrix
        
        Args : matrix - Matrix containing 0-255 numbers (ascii value of characters)
    """

    encoding_dictionary = {}
    for i in range(matrix.shape[0]) :
        for j in range(matrix.shape[1]) :
            row, col = i, j
            row_dig, col_dig = countDigit(row), countDigit(col)
            value = "0"*(3-row_dig)
            value += str(row)
            value += ("0"*(3-col_dig))
            value += str(col)
            encoding_dictionary[chr(matrix[row][col])] = value
    return encoding_dictionary
