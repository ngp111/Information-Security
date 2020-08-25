import numpy as np

from rotate_matrix import rot_90_clock, rot_90_anticlock, rot_180, swap_rows
from create_matrix import spiral_clockwise, spiral_anticlockwise

def create_mapping_matrix(key) :
    """
        Creates the matrix based on the key which will be used for encoding

        Args : key - Key which provides details on how to form the matrix
    """
    
    start_char = key['starting_char']
    
    dimensions = key['dimensions']
    
    spiral_direction = key['spiralDirection']
    
    degree = key['degree']
    
    rotation_direction = key['rotationDirection']
    
    swap = key['swap']
    
    matrix = np.zeros((dimensions[0], dimensions[1])).astype(int)
    
    if(spiral_direction == "clockwise") :
        spiral_clockwise(matrix, start_char)
    else :
        spiral_anticlockwise(matrix, start_char) 
    
    if(degree == 90) :
        if(rotation_direction == "clockwise") :
            matrix = rot_90_clock(matrix)
        else :
            matrix = rot_90_anticlock(matrix)
    else :
        matrix = rot_180(matrix)
        
    if(swap == 1) :
        matrix = swap_rows(matrix)

    return matrix
