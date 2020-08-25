import numpy as np

def rot_90_clock(matrix) :
    """
        Rotates the given matrix by 90 degrees in clockwise direction
    
        Args : matrix - the matrix that is to be rotated
    """
    return np.rot90(matrix, k = 3)

def rot_90_anticlock(matrix) :
    """
        Rotates the given matrix by 90 degrees in anticlockwise direction
    
        Args : matrix - the matrix that is to be rotated
    """
    return np.rot90(matrix, k = 1)
        
def rot_180(matrix) :
    """
        Rotates the given matrix by 180 degress

        Note : direction won't matter
    
        Args : matrix - the matrix that is to be rotated
    """
    return np.rot90(matrix, k = 2)

def swap_rows(matrix) :
    """
        Swap the 0th row with (n-1)st row, 
                 1st row with (n-2)nd row and so on

        Args : matrix - the matrix on which swapping is to be done
    """
    return matrix[:][::-1]
