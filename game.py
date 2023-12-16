'''
Todo: make a python script for playing tic - tac - toe game 
Author: Kapish Patel

How to run the game:
1. install python 
2. open the directory 
3. and run python3 game.py 

sample:
1. Run the command 
    python3 game.py
2. Enter usernames
    Enter Name of First Player :: kapish
    Enter Name of Second Player :: parth
3. loading screen
    Randomly selecting first player...
    \
4. Start playing game by entering cell numbers in input starting from 1-9
    Player 1: a, Player 2: s
    ┌─┬─┬─┐
    │1│2│3│
    ├─┼─┼─┤
    │4│5│6│
    ├─┼─┼─┤
    │7│8│9│
    └─┴─┴─┘
    Player 1, a is playing[O] move...
    Enter the cell number :: 
5. Results
    Draw match Output
    ┌─┬─┬─┐
    │O│X│O│
    ├─┼─┼─┤
    │X│X│O│
    ├─┼─┼─┤
    │O│O│X│
    └─┴─┴─┘
    
    O WINS Output
    ┌─┬─┬─┐
    │O│O│O│
    ├─┼─┼─┤
    │X│X│O│
    ├─┼─┼─┤
    │O│X│X│
    └─┴─┴─┘
    
    X WINS Output
    ┌─┬─┬─┐
    │X│X│O│
    ├─┼─┼─┤
    │O│X│O│
    ├─┼─┼─┤
    │O│O│X│
    └─┴─┴─┘
'''

# import statements 
# random for generating random numbers
# os for clearing screen
# time for sleep function
# enum for enum class
import random
import os
import time
from enum import Enum

# resolver dictionary which resolve cell number to cell location
RESOLVER = {
    1: (0,0), 2:(0,1), 3:(0,2),
    4: (1,0), 5:(1,1), 6:(1,2),
    7: (2,0), 8:(2,1), 9:(2,2),
}



# status enum class hold different status
class status(Enum):
    PROGRESS = "game in progress..."
    WIN_X = "Player X wins!"
    WIN_O = "Player O wins!"
    DRAW = "It's a draw!"



# tic tac toe class which hold all the operations from user
class TicTacToe:
    def __init__(self, users) -> None:
        # value of grid, board, and 8 winning conditions
        self.grid = TicTacToe.generate_empty_grid()
        self.board = self.generate_board() 
        self.winning_combinations = TicTacToe.generate_winning_combinations()
        
        # value of user, game status and move count
        self.users = [(users[0], 79),(users[1], 88)]
        self.game_status = status.PROGRESS.value
        self.current_player = 0 # 0 for player 1, 1 for player 2
        self.movecount = 1

        # start game
        self.game_start()

    # function to generate combination or winning conditions
    @staticmethod
    def generate_winning_combinations():
        return [[(0,0),(0,1),(0,2)],    # top row
                [(1,0),(1,1),(1,2)],    # mid row
                [(2,0),(2,1),(2,2)],    # bottom row
                [(0,0),(1,0),(2,0)],    # left column
                [(0,1),(1,1),(1,2)],    # mid column
                [(0,2),(1,2),(2,2)],    # right column
                [(0,0),(1,1),(2,2)],    # top left - bottom right diagonal
                [(0,2),(1,1),(2,0)]]    # top right - bottom left diagonal

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

    # function to check who is winning
    def check_win(self):
        # the logic is there are 8 winning possibilities check each possibility with the current version of user
        for combination in self.winning_combinations:   # combination from all the combinations
            if all(self.grid[i][j] == self.users[self.current_player][1] for i,j in combination):   # if all the 3 cells are filled with respective X, O then change the status of game
                self.game_status = status.WIN_O.value if self.current_player == 0 else status.WIN_X.value        
        
    # function to update the grid with X and O
    def update_grid(self, i, j):
        self.grid[i][j] = self.users[self.current_player][1]
        #check if any player is winning 
        if self.movecount >= 3:
            self.check_win()
        self.update_board()
        self.toogleplayer()

        if not any(9608 in row for row in self.grid):   # if the grid is full then change the status to draw
            self.game_status = status.DRAW.value

    # function to take player input
    def playerInput(self) -> (int, int):
            # print(f"input count:: {self.movecount}")
            cell_input = input("Enter the cell number :: ")
            cell_Number = int(cell_input)
            i,j = RESOLVER.get(cell_Number)
            if self.current_player == 1:
                self.movecount += 1
            return (i,j) if self.check_valid_input(i, j) else self.playerInput()    #return if input is valid
    
    #fucntion to decide player to play
    def decidePlayer(self):
        if self.current_player == 0:
            print(f"Player 1, {self.users[0][0]} is playing[{chr(self.users[0][1])}] move...")
        else:
            print(f"Player 2, {self.users[1][0]} is playing[{chr(self.users[1][1])}] move...")

    # function to display pattern
    @staticmethod
    def display_pattern():
        print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

    # function to display draw decision
    def display_draw(self):
        TicTacToe.display_pattern()
        print(f"{status.DRAW.value} well played {self.users[0][0]}, {self.users[1][0]}")
        TicTacToe.display_pattern()
    
    # function to diaplay winning player
    def display_win(self,char):
        TicTacToe.display_pattern()
        if char == 'X':
            print(f"{status.WIN_X.value} well played {self.users[1][0]}")
        else:
            print(f"{status.WIN_O.value} well played {self.users[0][0]}")
        TicTacToe.display_pattern()


    # function to display decision of the game
    def display_decision(self):
        self.display_Board()
        print(self.game_status)
        if self.game_status == status.DRAW.value:
            self.display_draw()
        elif self.game_status == status.WIN_O.value:
           self.display_win('O')
        else:
            self.display_win('X')
        
    # fucntion to start the game    
    def game_start(self):
        self.display_Users()
        self.display_Board()
        while self.game_status == status.PROGRESS.value:  #repeat this process till status changes
            self.decidePlayer()
            i,j = self.playerInput()
            os.system('clear')
            self.update_grid(i, j)
            self.display_Board()
        #print results
        os.system('clear')
        #call function which fancily print winner
        self.display_decision()

        

# user class takes user name and randomly decide first player
class User:
    def __init__(self) -> None:
        self.users = ['','']
        self.userInputs()
        self.random_select_firstplayer()

    # function for username input
    def userInputs(self):
        self.users[0] = input("Enter Name of First Player :: ")
        self.users[1] = input("Enter Name of Second Player :: ")    

    # function which retuns players data
    def get_players(self):
        return self.users
    
    # function to display loading screen
    @staticmethod
    def displayLoading():
        for i in range(0,10):
            User.printSleep('\\')
            User.printSleep('/')
            User.printSleep('-')

    # function to print and sleep
    @staticmethod
    def printSleep(char):
        print("Randomly selecting first player...")
        print(char)
        time.sleep(0.1)
        os.system('clear')

    # function to randomly select first player
    def random_select_firstplayer(self):
        User.displayLoading()
        randomNumber = random.randint(0,1)
        if randomNumber == 1:
            self.swapPlayer()

    # function to swap player
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

        