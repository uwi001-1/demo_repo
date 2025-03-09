height = 5  
width = (2 * height) - 1

#AAAAAAAAAAA
def printA(): 
    n = width // 2
    for i in range(0, height): 
        for j in range(0, width+1): 
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))): 
                print("*", end="") 
            else: 
                print(end=" ") 
        print() 
        n = n-1

#IIIIIIIIIIII
def printI() : 
    for i in range(0,height) : 
        for j in range(0,height) : 
            if ( i == 0 or i == height - 1 ): 
                print("*",end="") 
            elif ( j == height // 2 ) : 
                print("*",end="") 
            else : 
                print(end=" ") 
        print() 

#KKKKKKKKKKKK
def printK() : 
    half = height // 2
    dummy = half 
    for i in range(0,height) : 
        print("*",end="") 
        for j in range(0,half+1) : 
            if ( j == abs(dummy) ): 
                print("*",end="") 
            else : 
                print(end=" ") 
        print() 
        dummy = dummy -1

#PPPPPPPPPPPP
def printP() : 
    for i in range(0,height) : 
        print("*",end="") 
        for j in range(0,height) : 
            if ( (i == 0 or i == height // 2) and j < height - 1 ): 
                print("*",end="") 
            elif ( i < height // 2 and j == height - 1 and i != 0 ) : 
                print("*",end="") 
            else : 
                print(end=" ") 
        print() 

#RRRRRRRRRR
def printR() : 
    half = (height // 2) 
    for i in range(0,height) : 
        print("*",end="") 
        for j in range(0,width) : 
            if ( (i == 0 or i == half) and j < (width - 2) ): 
                print("*",end="") 
            elif ( j == (width - 2) and not(i == 0 or i == half) ) : 
                print("*",end="") 
            else : 
                print(end=" ") 
        print() 

printK()
printR()
printI()
printP()
printA()