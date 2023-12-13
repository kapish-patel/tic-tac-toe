'''
Todo: make a python script for playing tic - tac - toe game
Author: Kapish Patel
'''
import random
import os
import time
from enum import Enum


RESOLVER = {
    1: (0,0), 2:(0,1), 3:(0,2),
    4: (1,0), 5:(1,1), 6:(1,2),
    7: (2,0), 8:(2,1), 9:(2,2),
}

# status enum class hold different status
class status(Enum):
    PROGRESS = "game in progress..."
    PENDING = "decision pending..."
    WIN_X = "Player X wins!"
    WIN_O = "Player O wins!"
    DRAW = "It's a draw!"


# tic tac toe class which hold all the operations from user
class TicTacToe:
    def __init__(self, users) -> None:
        # value of grid, board and user
        self.grid = TicTacToe.generate_empty_grid()
        self.board = self.generate_board() 
        
        self.users = [(users[0], 79),(users[1], 88)]
        self.game_status = status.PROGRESS
        self.current_player = 0

        self.display_Users()
        self.display_Board()
        # start game
        self.game_start()

    # function to generate grid just the X's and O's
    @staticmethod
    def generate_empty_grid():
        return [[9608,9608,9608],  # update these values to X,O depending on user input
                [9608,9608,9608],
                [9608,9608,9608],]

    # function to generate board includes the gird and outline
    def generate_board(self):
        return [[9484, 9472, 9516, 9472, 9516, 9472, 9488],   # board is the design with the values of grid display this
                [9474, self.grid[0][0], 9474, self.grid[0][1], 9474, self.grid[0][2], 9474],
                [9500, 9472, 9532, 9472, 9532, 9472, 9508],
                [9474, self.grid[1][0], 9474, self.grid[1][1], 9474, self.grid[1][2], 9474],
                [9500, 9472, 9532, 9472, 9532, 9472, 9508],
                [9474, self.grid[2][0], 9474, self.grid[2][1], 9474, self.grid[2][2], 9474],
                [9492, 9472, 9524, 9472, 9524, 9472, 9496]]  

    # fucntion to display board
    def display_Board(self):
        for i in range(0, len(self.board)):   #row
            for j in range(0, len(self.board[0])):    #column
                print(chr(self.board[i][j]), end='')
            print(end='\n')

    # function to display users
    def display_Users(self):
        print(f"Player 1: {self.users[0][0]}, Player 2: {self.users[1][0]}")

    # function to switch current player
    def toogleplayer(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0

    # function to check user input if the cell is alreay full or not
    def check_valid_input(self, i, j) -> bool: 
        if self.grid[i][j] in [79,88]:
            return False
        return True
    
    #function to update the board
    def update_board(self):
        self.board = self.generate_board()

    # function to update the grid with X and O
    def update_grid(self, i, j):
        self.grid[i][j] = self.users[self.current_player][1]
        self.update_board()
        self.toogleplayer()

        if not any(9608 in row for row in self.grid):
            self.game_status = status.PENDING

    # function to take player input
    def playerInput(self) -> (int, int):
            cell_input = input("Enter the cell number :: ")
            cell_Number = int(cell_input)
            i,j = RESOLVER.get(cell_Number)
            return (i,j) if self.check_valid_input(i, j) else self.playerInput()    #return if input is valid

    #fucntion to decide player to play
    def decidePlayer(self):
        if self.current_player == 0:
            print(f"Player 1, {self.users[0][0]} is playing[{chr(self.users[0][1])}] move...")
        else:
            print(f"Player 2, {self.users[1][0]} is playing[{chr(self.users[1][1])}] move...")
        
    # fucntion to start the game    
    def game_start(self):
        while self.game_status == status.PROGRESS:
            self.decidePlayer()
            i,j = self.playerInput()
            self.update_grid(i, j)
            self.display_Board()
        if self.game_status == status.PENDING:
            print("decision pending..........")     # start working here make logic for decision making also think of updating the update grid function think of real testing 
        

class User:
    def __init__(self) -> None:
        self.users = ['','']
        self.userInputs()
        self.random_select_firstplayer()

    def userInputs(self):
        self.users[0] = input("Enter Name of First Player :: ")
        self.users[1] = input("Enter Name of Second Player :: ")    

    def get_players(self):
        return self.users
    
    @staticmethod
    def test_print(i):
        print(chr(i), end=" ")
    
    @staticmethod
    def displayLoading():
        for i in range(0,10):
            User.printSleep('\\')
            User.printSleep('/')
            User.printSleep('-')

    @staticmethod
    def printSleep(char):
        print("Randomly selecting first player...")
        print(char)
        time.sleep(0.1)
        os.system('clear')

    def random_select_firstplayer(self):
        User.displayLoading()
        randomNumber = random.randint(0,1)
        if randomNumber == 1:
            self.swapPlayer()

    def swapPlayer(self):
        temp = self.users[0]
        self.users[0] = self.users[1]
        self.users[1] = temp
    
# main function
def main():
    user = User()
    users = user.get_players()
    game = TicTacToe(users)


if __name__ == "__main__":
    main()

        