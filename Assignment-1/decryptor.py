import socket  
import pickle              

from rotate_string import right_shift, left_shift
from map_characters import generate_codes
from generate_matrix import create_mapping_matrix

def decrypt(message) :
    """
        1. Get the key from message
        2. Create matrix 
        3. Make the codes dictionary mapping character to the position in matrix
        4. Undo the shift done by encryptor using key values
        5. Traverse through message and get positions of character to be accessed
	6. Get the character using positions and complete the message

        Args : message - message to be decrypted

        Constraint : Each character is represented by 6 digits : 3 for row number, and 3 for column number
                     as maximum value of row/column number can be 255.
    """
 
    key = message['key']
    message = message['encrypted_message'] 

    matrix = create_mapping_matrix(key)
    
    encoding_dictionary = generate_codes(matrix)
    
    if(key['shift_direction'] == "clockwise") :
        message = left_shift(message, key['shift'])
    else :  
        message = right_shift(message, key['shift'])
    
    decrypted_message = ""
    for i in range(0, len(message)-5, 6) :
        row =int(message[i:i+3])
        col = int(message[i+3:i+6])
        decrypted_message += chr(matrix[row][col])
    
    file = open("decrypted.txt", "w")
    file.write(decrypted_message)
    file.close()
 
def main() :
	"""
        	Receives the encrypted message, and key needed to decrypt the message
                using sockets.  
        """

	s = socket.socket()          
	print("Socket successfully created")
	 
	port = 12345                 
	s.bind(('', port))         
	print("socket binded to %s" %(port))

	s.listen(5)      
	print("socket is listening")   
	
	while True: 
		c, addr = s.accept() 
		print('Got connection from', addr)
		message = pickle.loads(c.recv(800000))
		decrypt(message)
		c.close()
		

if __name__ == "__main__":
    main()
