"""
board
print board continuously 
take user input: only if there's no win or draw
generate computer input: only if there's no win or draw
win: diagonal, column, row
draw: when board is full and no win 
"""
import random
board= ['','','','','','','','','']
def printboard():
    print(board[0],'|',board[1],'|',board[2])
    print('------')
    print(board[3],'|',board[4],'|',board[5])
    print('------')
    print(board[6],'|',board[7],'|',board[8])

def edittable(move,moveinput):
    board[move]= moveinput

def available(move):
    if board[move]== '':
        return True
    else:
        return False
def win(board,moveinput):
    if (board[0]==moveinput and board[1]== moveinput and board[2]== moveinput) or (board[3]==moveinput and board[4]== moveinput and board[5]== moveinput) or (board[6]==moveinput and board[7]== moveinput and board[8]== moveinput) or (board[0]==moveinput and board[3]== moveinput and board[6]== moveinput) or (board[1]==moveinput and board[4]== moveinput and board[7]== moveinput) or (board[2]==moveinput and board[5]== moveinput and board[8]== moveinput) or (board[0]==moveinput and board[4]== moveinput and board[8]== moveinput) or (board[2]==moveinput and board[4]== moveinput and board[6]== moveinput):
        return True
    else:
        return False
def draw():
    if board.count('')>=1:
        return False
    if win(board,'x'):
        return False
    if win(board,'o'):
        return False
    else:
        return True

def playerinput():
    game=True
    while game:
    
        move=input('Please enter coordinate where you want to place an X (0-8):')
        #try,except: 
        try:
            move=int(move)
            if not available(move):
                    print('This position is occupied, please enter an empty position')
            elif move>8 or move<0:
                print("Enter number in range!")
            else:
                game=False
                edittable(move,'x')
                


        except: 
            print('Invalid Input!')
def computermove():
    #IMPORTANT
    availablemoves= [x for x,value in enumerate(board) if value=='']
    compmove=10
    for letter in ['x','o']:
         
        for i in availablemoves:
            boardcopy=board[:] #------> to ensure it's a completely diff copy of board, upon changing boardcopy no change in board
            boardcopy[i]= letter
            if win(boardcopy, letter):
                compmove= i 
                return compmove
            


    availablecorners=[]
    for i in availablemoves:
         if i in [0,2,6,8]:
            availablecorners += [i]
            
    if len(availablecorners)>0:

        compmove= random.choice(availablecorners)
            
        return compmove
            
    if 4 in availablemoves:
                
        compmove=4
        return compmove      
                
    
    
            
    availableedges=[]
    for i in availablemoves:
        if i in [1,3,5,7]:
            availableedges += [i]
    if len(availableedges)>0:

        compmove= random.choice(availableedges)
            
        return compmove
    



while not draw():
    printboard()
    if not win(board,'o'):
        playerinput()
           
    else:
        print('Computer wins!')
        break
    if not win(board,'x'):
        compinput=computermove()
        if compinput== 10:

            print('Its a Tie!')
            break
        else:
            edittable(compinput, 'o')
    else:
        printboard()
        print('Congrats, you won!')
        
        break