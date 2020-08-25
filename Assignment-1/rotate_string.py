def right_shift(message, shift) :
    """
        Circular shift the message by given shift to the right (clockwise shift)

        Args : message - String that is to be shifted
               shift - Amount by which the message is to be shifted
    """
    return message[-shift:] + message[:-shift]

def left_shift(message, shift) :
    """
        Circular shift the message by given shift to the left (anticlockwise shift)

        Args : message - String that is to be shifted
               shift - Amount by which the message is to be shifted
    """
    n = len(message)
    first = message[0:shift][::-1]
    second= message[shift:n][::-1]
    message = (first+second)[::-1]
    return message
