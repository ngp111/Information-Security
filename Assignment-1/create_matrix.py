def spiral_clockwise(a, start_val):
    """
        Fills the matrix "a" with values starting from start_val
        in a spiral inwards clockwise direction from (0, 0) position.

        Repeat : [right -> down -> left -> up]
        
        Constraint: Values in matrix are mod 256 - representing ascii values of characters
        Args : a - 2D matrix
               start_val - value with which to start filling the matrix
    """

    direction = "right"
    val =start_val%256
    sr, sc = 0, 0
    er = a.shape[0]
    ec = a.shape[1]
    while(sr<er and sc<ec) :
        if(direction == "right") :
            for i in range(sc, ec) :
                a[sr][i] = val
                val = (val+1)%256
            sr += 1
            direction = "down"
        elif(direction == "down") :
            for i in range(sr, er) :
                a[i][ec-1] = val
                val = (val+1)%256
            ec -= 1
            direction = "left"
        elif(direction == "left") :
            for i in range(ec-1, sc-1, -1) :
                a[er-1][i] = val
                val = (val+1)%256
            er -= 1
            direction = "up"
        else :
            for i in range(er-1, sr-1, -1) :
                a[i][sc] = val
                val = (val+1)%256
            sc += 1
            direction = "right"
            

def spiral_anticlockwise(a, start_val):
    """
        Fills the matrix "a" with values starting from start_val
        in a spiral inwards anticlockwise direction from (0, 0) position.

        Repeat : [down -> right -> up -> left]
        
        Constraint: Values in matrix are mod 256 - representing ascii values of characters
        Args : a - 2D matrix
               start_val - value with which to start filling the matrix
    """
    direction = "down"
    val =start_val%256
    sr, sc = 0, 0
    er = a.shape[0]
    ec = a.shape[1]
    while(sr<er and sc<ec) :
        if(direction == "down") :
            for i in range(sr, er) :
                a[i][sc] = val
                val = (val+1)%256
            sc += 1
            direction = "right"
        elif(direction == "right") :
            for i in range(sc, ec) :
                a[er-1][i] = val
                val = (val+1)%256
            er -= 1
            direction = "up"
        elif(direction == "up"):
            for i in range(er-1, sr-1, -1) :
                a[i][ec-1] = val
                val = (val+1)%256
            ec -= 1
            direction = "left"
        else :
            for i in range(ec-1, sc-1, -1) :
                a[sr][i] = val
                val = (val+1)%256
            sr += 1
            direction = "down"

