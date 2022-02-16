Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random

def frame_score(tow,bis):
    """This function gets the final scores and prints them in an asterisc frame"""
    print('*' * 17)
    print('* Black * White *')
    print('*' * 17) 
    print('*' + ' ' * 7 + '*' + ' ' * 7 + '*')
     
    #Solely for design purposes:  
    if (tow>9 and bis>9):
            print('*  {}   *   {}  *'.format(bis,tow))
    elif (tow>9 and bis<=9):
            print('*   {}   *   {}  *'.format(bis,tow))
    elif (tow<=9 and bis>9):
            print('*   {}  *   {}   *'.format(bis,tow))
    else:
           print('*  {}    *   {}   *'.format(bis,tow))
       
    print('*' + ' ' * 7 + '*' + ' ' * 7 + '*')     
    print('*' * 17 +'\n\n')

    
def oneTo(i):
    """This function generates a random number between 1 and i"""
    r=random.randint(1,i)
    return r

round=0 #number of rounds played
game=0 #0 means 8*8, 1 means 7*7, 2 means 7*8  
tower_score=0 #(White) Tower's Score
bishop_score=0 #(Black) Bishop's Score

#As in actual chess, white goes first. 
#That means that white plays in every odd round (1,3,5 etc)  


############ The game ############
while (round<100):
    
    round+=1
    
    #To find the white tower's and black bishop's random coordinates:
    if (game==0):
        tower_row = oneTo(8)
        tower_column= oneTo(8)
        bishop_row = oneTo(8)
        bishop_column = oneTo(8)
    
        #In case the pawns' positions overlap       
        while (tower_row == bishop_row and tower_column == bishop_column):
            bishop_column= oneTo(8)
        
    elif (game==1):
        tower_row = oneTo(7)
        tower_column= oneTo(8)
        bishop_row = oneTo(7)
        bishop_column = oneTo(8)
        
        #In case the pawns' positions overlap 
        while (tower_row == bishop_row and tower_column == bishop_column):
            bishop_column= oneTo(8)
    
    else:
        tower_row = oneTo(7)
        tower_column= oneTo(7)
        bishop_row = oneTo(7)
        bishop_column = oneTo(7)
    
        #In case the pawns' positions overlap 
        while (tower_row == bishop_row and tower_column == bishop_column):
             bishop_column= oneTo(8)

    #If it is white's turn to play:
    if (round % 2 == 1): 
        #If the tower can capture the bishop:
        if (tower_row == bishop_row or tower_column == bishop_column):
            tower_score+=1
            
    #If it is black's turn to play:
    else:
        #If the bishop can capture the tower:
        if (abs(tower_row - bishop_row) == abs(tower_column - bishop_column)):
            bishop_score+=1
    
    #If the final round has been played
    if (round==100):
        round=0
        
        #If the variable "game" is equal to 0, the game is 8*8
        if (game==0):
            print("The score of the 8x8 game is:")
            
        #If the variable "game" is equal to 1, the game is 7*7 
        elif (game==1):
            print("The score of the 7x7 game is: ")
            
        #If the variable "game" is equal to 2, the game is 7*8
        else:
            print("The score of the 7x8 game is: ")
        
        #The score is printed
        frame_score(tower_score,bishop_score)
        game+=1
        tower_score=0
        bishop_score=0
        
        #If all three games have ended, terminate the program 
        if (game==3):
            break