import socket	
import sys		 
import random
import pickle

from rotate_string import right_shift, left_shift
from map_characters import generate_codes
from generate_matrix import create_mapping_matrix

def encode(matrix, msg) :
    """
        Using the encoding dictionary, maps characters from message to their codes
    """
    encoding_dictionary = generate_codes(matrix)
    sample = msg
    message = ""
    for char in sample :
        message += encoding_dictionary[char]
    return message     

def generate_key(max_shift) : 
    """
        Create a key with fields : starting_char, dimensions, 
                                   spiralDirection, degree, rotationDirection, 
                                   swap, shift, shift_direction
        Args : max_shift - used when generating shift
 
        Constraints - starting_char = [0,256); 
                      dimensions = [(1, 256), (2, 128), (4, 64), (8, 32), (16, 16), 
                                    (32, 8), (64, 4), (128, 2), (256, 1)]
                      spiralDirection = [clockwise, counterclockwise]
                      degree = [90, 180]
                      rotationDirection = [clockwise, counterclockwise]
                      swap = [0,1]
                      shift = [0, max_shift)
                      shift_direction = [clockwise, counterclockwise]
    """
    key = {}
    
    directions = ["clockwise", "counterclockwise"]
    
    start_char = random.randint(0, 256)
    dim = random.choice([1, 2, 4, 8, 16, 32, 64, 32, 256]) 
    spiral_direction = directions[random.choice([0, 1])]
    degree = random.choice([90, 180])
    if(degree == 90) :
        rotation_direction = directions[random.choice([0, 1])]
    
    key['starting_char'] = start_char
    key['dimensions'] = (dim, 256//dim)
    key['spiralDirection'] = spiral_direction
    key['degree'] = degree
    key['rotationDirection'] = rotation_direction if degree == 90 else ""
    key['swap'] = random.choice([0, 1])
    key['shift'] = random.randint(0, max_shift)
    key['shift_direction'] = directions[random.choice([0, 1])]
    
    return key

def encrypt(msg) :
    """
        1. Generate a random key
        2. Create a encoding matrix using the generated key
        3. Encode the message based on the codes using matrix created
        4. Circular shift the message by shift, and in shift_direction based on the key generated.
 
        Args : msg - Message that is to be encrypted
    """
    key = generate_key(len(msg))
    matrix = create_mapping_matrix(key)
    to_send = encode(matrix, msg)
    
    if(key['shift_direction'] == "clockwise") :
        to_send = right_shift(to_send, key['shift']) 
    else :
        to_send = left_shift(to_send, key['shift']) 
    return (key, to_send)

def main() :
	"""
        	Sends the encrypted message, and key needed to decrypt the message
                using sockets
	"""
	#Encryption testing file
	filename = sys.argv[1]
	file = open(filename)
	content = file.read()
	file.close()
	
	key, msg = encrypt(content)
	message_to_send = {}
	message_to_send['key'] = key
	message_to_send['encrypted_message'] = msg
	
	s = socket.socket()		 
	port = 12345				

	s.connect(('127.0.0.1', port)) 

	s.send(pickle.dumps(message_to_send))
	s.close()

if __name__ == "__main__":
    main()
