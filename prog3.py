#!/usr/bin/python3

'''# implement a N Queens recursive Python program                         #
#               Assignment3 CS503                                          #
#               Completed Date: 3/21/2019                                  #
#               Developer: Leela Krishna Vasista Gutta                     #
#               ZID: Z1839489                                              #'''

import sys
from time import time
from random import seed, randint

def driver():
    '''It starts the program by calling the routine solveNQueens ( ), as explained
below, for each value of N, between 1 and 8, to place the N queens on the chessboard'''
    for n in range(1,9):  #Iterating N Values from 1 to 8
         solveNQueens(n)  #Calling the solveQueens Method
         sys.stdout.write("\n")



def initBoard(N):
    ''' Initializes a RNG with a chosen seed value.It also creates a two-dimensional list (matrix)
for the board of size N and sets all positions on the board to False and returns the
initial board to the following routine'''
    seed(time())        #calling seed function for random numbers and passing time() method
    board = [[False]*N for _ in range(N)]   #Intializing the board with False
    return board                    #Returns the intialize board



def solveNQueens(N):
    '''To place the N queens on the board, starting from the first row, it
prints out the board size and calls to routine solveNQueensUtil ( ), as explained
below. If the returned value of solveNQueensUtil ( ) is True, then it calls the routine
printBoard ( ) to print out the contents of the board on stdout by showing the
positions of the queens on the board, otherwise, it prints a message indicating that
a solution does not exists.'''
    sys.stdout.write("Board size = "+str( N)+"\n")   #Printing the Size of Board
    board = initBoard(N)                            
    if solveNqueensUtil(board,0)== True:            #If chess board has the solution then returns True
        printBoard(board)                           #calling the  formated chess board
    else:
        sys.stdout.write("Solution does not exist.\n") #If no solution doesnot exist


def solveNqueensUtil(board, row):
    '''This recursive routine starts on the row number
row and gets a random column number col, between 0 and ( size ( board ) – 1 ) from
the RNG,and it checks if a queen can be placed on the location ( row, col ). It calls the routine isSafe ( ),
which is explained below, to determine if the location is safe, so the queen can be
placed in that location. '''
    if row >= len(board):  #//If all queens have been successfully placed then return true.
        return True
    col = randint(0,len(board)-1) #Using random package choosing the random column in a row
    for i in range(len(board)): 
        if i==0:
            if isSafe(board,row,col):       #If safe to place the queen in a row 
                board[row][col]=True        #then insert the true in that row and col position
                
                if solveNqueensUtil(board, row+1):  # Then call the recursion for next row
                    return True
                else:
                    board[row][col] = False         #place the false not safe situation
                
        if i!=col:
            if isSafe(board,row,i):
                board[row][i]=True
                col = randint(0,len(board)-1)
                if solveNqueensUtil(board, row+1):
                    return True
                else:
                    board[row][i] = False
    return False 



def isSafe(board, row, col):
    ''': It checks if a queen can be placed in the row number row
and the column number col on the board. If the answer is “yes”, then it returns
True'''
    for r in range(0,row):
        for c in range(0,len(board)):
            if board[r][c] and (c==col or abs(c-col)== abs(r-row)): #Checks the Q is same col or row or in diagnal 
                return False
    return True




def printBoard(board):
    '''It prints the final state of the board as a properly-formatted
rectangular table'''
    N = len(board)           #Gives the Sixe of board
    cal=(N*6)-1             # calcualting for printing number of '-' on the top of each row  
    for i in range(N):      # Row iteration
        sys.stdout.write(" "+'-'*cal+" \n")  #Printing '-'
        for k in range(1,4):                 #Iteration for 3 horizontal lines   
            for j in range(N):              # Iteration for columns
                sys.stdout.write("|")
                if(k==2):                   #Placing the Q in the middle horizontal line in a row
                    if board[i][j] == True:
                        sys.stdout.write("  Q  ")
                    else:
                        sys.stdout.write("     ")
                else:
                    sys.stdout.write("     ")
            sys.stdout.write("|\n")
    sys.stdout.write(" "+'-'*cal+" \n")    

driver()  #function call to start the program
