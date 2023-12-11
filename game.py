'''
Todo: make a python script for playing tic - tac - toe game
Author: Kapish Patel
'''

# tic tac toe class which hold all the operations from user
class TicTacToe:
    def __init__(self) -> None:
        self.board = [[9484, 9472, 9516, 9472, 9516, 9472, 9488],
                      [9474, 9617, 9474, 9617, 9474, 9617, 9474],
                      [9500, 9472, 9532, 9472, 9532, 9472, 9508],
                      [9474, 9617, 9474, 9617, 9474, 9617, 9474],
                      [9500, 9472, 9532, 9472, 9532, 9472, 9508],
                      [9474, 9617, 9474, 9617, 9474, 9617, 9474],
                      [9492, 9472, 9524, 9472, 9524, 9472, 9496]]
        # print("Current board:", self.board)
        
    def display_Board(self):
        for i in range(0, len(self.board)):   #row
            for j in range(0, len(self.board[0])):    #column
                print(chr(self.board[i][j]), end='')
            print(end='\n')
    

def test_print(i):
    print(chr(i), end=" ")
# main function
def main():
   game = TicTacToe()
   game.display_Board()
if __name__ == "__main__":
    main()

        