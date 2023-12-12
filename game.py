'''
Todo: make a python script for playing tic - tac - toe game
Author: Kapish Patel
'''
import random
import os
import time

# tic tac toe class which hold all the operations from user
class TicTacToe:
    def __init__(self, users) -> None:
        self.grid = [[9608,9608,9608],  # update these values to X,O depending on user input
                     [9608,9608,9608],
                     [9608,9608,9608],]
        
        self.board = [[9484, 9472, 9516, 9472, 9516, 9472, 9488],   # board is the design with the values of grid display this
                      [9474, self.grid[0][0], 9474, self.grid[0][1], 9474, self.grid[0][2], 9474],
                      [9500, 9472, 9532, 9472, 9532, 9472, 9508],
                      [9474, self.grid[1][0], 9474, self.grid[1][1], 9474, self.grid[1][2], 9474],
                      [9500, 9472, 9532, 9472, 9532, 9472, 9508],
                      [9474, self.grid[2][0], 9474, self.grid[2][1], 9474, self.grid[2][2], 9474],
                      [9492, 9472, 9524, 9472, 9524, 9472, 9496]]   
        
        self.users = users
        print(f"player 1: {self.users[0]}, player 2: {self.users[1]}")

    def display_Board(self):
        for i in range(0, len(self.board)):   #row
            for j in range(0, len(self.board[0])):    #column
                print(chr(self.board[i][j]), end='')
            print(end='\n')
    

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

        